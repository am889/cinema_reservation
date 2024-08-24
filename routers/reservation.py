# from .movies import *
# from fastapi import Form
# router = APIRouter()



# @router.post('/reservation',status_code=status.HTTP_201_CREATED, response_class=HTMLResponse)
# async def reserve(db:db_dependency,reservationrequest:ReservationRequest,user:user_dependency,request:Request):
#     if user is None:
#         raise HTTPException(status_code=401,detail='Authentication Failed')
#     reservation_model=Reservations(**reservationrequest.model_dump(),user_id=user.get('id'))
#     db.add(reservation_model)
#     db.commit()
#     return (templates.TemplateResponse("book.html",{'request':request}))


# @router.post('/reservation', response_class=HTMLResponse)
# async def reserve(db:db_dependency,reservationrequest:ReservationRequest,user:user_dependency,request:Request,):
#     if user is None:
#         raise HTTPException(status_code=401,detail='Authentication Failed')
#     reservation_model=Reservations(**reservationrequest.model_dump(),user_id=user.get('id'))
#     db.add(reservation_model)
#     db.commit()
#     return (templates.TemplateResponse("book.html",{'request':request}))