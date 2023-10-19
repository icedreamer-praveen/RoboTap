from fastapi import FastAPI
import models
import database
from routers import robo

engine = database.engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(robo.router)

