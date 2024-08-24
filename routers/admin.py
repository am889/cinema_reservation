from fastapi import APIRouter,Depends, HTTPException,Path,status
from sqlalchemy.orm import Session
from models import *
from typing import Annotated
from pydantic import BaseModel,Field
from database import SessionLocal
from .auth import get_current_user
from datetime import date, datetime


router = APIRouter(   
    prefix='/auth',
    tags=['auth']
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency =Annotated[Session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]