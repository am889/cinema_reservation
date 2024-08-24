from fastapi import APIRouter,Depends, HTTPException,Path,status,Request
from sqlalchemy.orm import Session
from models import *
from typing import Annotated
from pydantic import BaseModel,Field
from database import SessionLocal
from .auth import get_current_user
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from .requestclasses import *
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency =Annotated[Session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]
templates = Jinja2Templates(directory='templates')


@router.get('/test')
async def test(request:Request,db:db_dependency):
    movies= db.query(Movies).all()
    return templates.TemplateResponse("home.html",{"request":request,"movies":movies})


@router.post('/add_movie',status_code=status.HTTP_201_CREATED)
async def add_movie(db:db_dependency,movie_request:MovieRequest):
    movie_model= Movies(**movie_request.model_dump())
    db.add(movie_model)
    db.commit()

@router.get('/',status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Movies).all()
@router.get('/reservation/{movie_id}',response_class=HTMLResponse)
async def resrvation(request:Request,movie_id:int,db:db_dependency):
    
    user= await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth/login",status_code=status.HTTP_302_FOUND)
    movie_model = db.query(Movies).filter(Movies.id==movie_id).first()
    showtimes=db.query(ShowTimes).filter(movie_model.id==ShowTimes.movie_id).all()
    return templates.TemplateResponse("reservation.html",{"request":request,"movie_model":movie_model,"movie_id":movie_id,"showtimes":showtimes})
    

@router.put("/movies/{movie_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_movie(db:db_dependency,movie_id:int,movie_request:MovieRequest):
    movie_model=db.query(Movies).filter(Movies.movie_id==movie_id).first()
    if movie_id is None:
        raise HTTPException(status_code=404,detail='Movie Not Found')
    movie_model.movie_title= movie_request.movie_title
    movie_model.movie_description= movie_request.movie_description
    movie_model.duration= movie_request.duration
    db.add(movie_model)
    db.commit()

@router.delete("/movie/{movie_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(db:db_dependency,movie_id:int):
    movie_model= db.query(Movies).filter(Movies.id==movie_id).first()
    if movie_id is None:
        raise HTTPException(status_code=404,detail='Movie Not Found')
    db.delete(movie_model)
    db.commit()

@router.get('/movies/{movie_id}',status_code=status.HTTP_200_OK)
async def read_movie(db:db_dependency,movie_id:int = Path(gt=0)):
    movie_model= db.query(Movies).filter(Movies.id== movie_id).first()
    if movie_model is not None:
        return movie_model
    raise HTTPException(status_code=404,detail='Movie Not Found')

@router.post('/showtimes',status_code=status.HTTP_201_CREATED)
async def  add_showtime(db:db_dependency,showtimerequest:ShowTimeRequest):
    show_time_model=ShowTimes(**showtimerequest.model_dump())
    db.add(show_time_model)
    db.commit()

@router.post('/theater',status_code=status.HTTP_201_CREATED)
async def  add_theater(db:db_dependency,theaterrequest:TheaterRequest):
    theater_model=Theater(**theaterrequest.model_dump())
    db.add(theater_model)
    db.commit()

@router.post('/seats',status_code=status.HTTP_201_CREATED)
async def add_seats(db:db_dependency,seatsrequest:SeatsRequest):
    seats_model=seats(**seatsrequest.model_dump())
    db.add(seats_model)
    db.commit()

@router.post('/reservation',status_code=status.HTTP_201_CREATED)
async def reserve(db:db_dependency,reservationrequest:ReservationRequest,user:user_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    reservation_model=Reservations(**reservationrequest.model_dump(),user_id=user.get('id'))
    db.add(reservation_model)
    db.commit()