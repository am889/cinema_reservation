import sys
sys.path.append("...")
from datetime import datetime, timedelta
from typing import Annotated, Optional
from fastapi import APIRouter,Depends, Response,status,HTTPException,Request
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from pydantic import BaseModel
from models import Users
from database import SessionLocal
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt ,JWTError
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router= APIRouter(
    prefix='/auth',
    tags=['auth']
)
bcrypt_context =CryptContext(schemes=['bcrypt'],deprecated='auto')

SECRET_KEY='0190f89e6eea34a6a768d7d95df196b6a6a470bbd2303e27292476e2b9b8d007'
ALGORITHM='HS256'
oaut2_bearer= OAuth2PasswordBearer(tokenUrl='auth/token') 
templates = Jinja2Templates(directory='templates')



def authenticate_user(username:str,password:str,db):
    user= db.query(Users).filter(Users.username==username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.password_hash):
        return False
    return user

def create_access_token(username:str,user_id:int,role:str,expires_delta:timedelta):
    encode={'sub':username,'id':user_id,'role':role}
    expires=datetime.utcnow()+expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

async def get_current_user(request:Request):
    try:
        token = request.cookies.get("access_token")
        if token is None:
            return None
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        user_id:int=payload.get("id")
        user_role:str = payload.get("role")
        if username is None or user_id is None:
            return None
        return {'username':username,'id':user_id,'user_role':user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Could not validate user')



class Token(BaseModel):
    access_token:str
    token_type:str


class LoginForm:
    def __init__(self,request:Request):
        self.request:Request =request
        self.username:Optional[str]=None
        self.password:Optional[str]=None

    async def create_oauth_form(self):
        form= await self.request.form()
        self.username= form.get("username")
        self.password= form.get("password")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency =Annotated[Session,Depends(get_db)]

class CreateUserRequest(BaseModel):
    username:str
    email:str
    first_name:str
    last_name :str
    mobile:str
    password:str
    role:str


@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,create_user_request:CreateUserRequest):
    create_user_model= Users(
        email =create_user_request.email,
        username =create_user_request.username,
        first_name =create_user_request.first_name,
        last_name =create_user_request.last_name,
        mobile =create_user_request.mobile,
        password_hash =bcrypt_context.hash(create_user_request.password),
        role =create_user_request.role,
        is_active=True
    )
    db.add(create_user_model)
    db.commit()


    
    

@router.post("/token",response_model=Token)
async def login_for_access_password(response:Response,form_data: OAuth2PasswordRequestForm=Depends(),db: Session = Depends(get_db)):
    user= authenticate_user(form_data.username,form_data.password,db)
    if not user :
        return False
    
    token=create_access_token(user.username,user.id,user.role,timedelta(minutes=60))
    response.set_cookie(key="access_token",value=token,httponly=True)
    return True

@router.get("/login",response_class=HTMLResponse)
async def authentication_page(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@router.post("/login", response_class=HTMLResponse)
async def login(request: Request, db: Session = Depends(get_db)):
    try:
        form = LoginForm(request)
        await form.create_oauth_form()
        response = RedirectResponse(url="/test",status_code=status.HTTP_302_FOUND)
        validate_user_cookie = await login_for_access_password(response=response, form_data=form, db=db)
        if not validate_user_cookie:
            msg = "Incorrect email or password"
            return templates.TemplateResponse("login.html", {"request": request, "msg": msg})
        return response
    except HTTPException:
        msg = "Unknown error"
        return templates.TemplateResponse("login.html", {"request": request, "msg": msg})

    