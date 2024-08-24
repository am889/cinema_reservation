from pydantic import BaseModel,Field
from datetime import date, datetime

class MovieRequest(BaseModel):

    movie_title: str
    movie_description :str =Field(min_length=10)
    duration:str
    poster_url:str
    
    

class ShowTimeRequest(BaseModel):

    theater_id: int
    movie_id :int 
    start_time:datetime
    end_time:datetime

class TheaterRequest(BaseModel):

    name:str
    location:str
    capacity:int

class SeatsRequest(BaseModel):
    theater_id:int
    row_number:str
    seat_number:str
    
class ReservationRequest(BaseModel):
    showtime_id:int
    seat_id:int
    reservation_date:date
    status:str