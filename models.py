from database import Base
from sqlalchemy import Column,Integer,String,DateTime,Date,Time,Boolean,ForeignKey
from passlib.context import CryptContext

class Movies(Base):
    __tablename__='movies'
    id = Column(Integer,primary_key=True,index=True)
    movie_title=Column(String)
    movie_description=Column(String)
    duration=Column(String)
    poster_url=Column(String)

class Theater(Base):
    __tablename__='theater'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    location = Column(String)
    capacity = Column(Integer,nullable=True)

class ShowTimes(Base):
    __tablename__='show_times'
    id =Column(Integer,primary_key=True,index=True)
    movie_id =Column(Integer,ForeignKey("movies.id"))
    theater_id =Column(Integer,ForeignKey("theater.id"))
    start_time=Column(DateTime)
    end_time=Column(DateTime)
    price = Column(Integer,nullable=True)
    total_seats = Column(Integer,nullable=True)

class Reservations(Base):
    __tablename__='reservations'
    id =Column(Integer,primary_key=True,index=True)
    showtime_id = Column(Integer,ForeignKey('show_times.id'))
    user_id = Column(Integer,ForeignKey('users.id'))
    seat_id = Column(Integer,ForeignKey('seats.id'))
    reservation_date = Column(Date)
    status = Column(String)
    price = Column(Integer,nullable=True)

class seats(Base):
    __tablename__='seats'
    id =Column(Integer,primary_key=True,index=True)
    theater_id =Column(Integer,ForeignKey("theater.id"))
    row_number = Column(String)
    seat_number=Column(String)
    is_booked =Column(Boolean,default=False)

class Users(Base):
    __tablename__='users'
    id =Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    first_name = Column(String)
    last_name = Column(String)
    mobile = Column(String)
    password_hash=Column(String)
    is_active = Column(Boolean,default=True)
    role = Column(String)


