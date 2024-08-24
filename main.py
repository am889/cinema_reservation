from fastapi import FastAPI
import models
from database import engine
from routers import auth,movies
from starlette.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount('/static',StaticFiles(directory='static'),name='static')
app.mount("/images", StaticFiles(directory="images"), name="images")


app.include_router(auth.router)
app.include_router(movies.router)
