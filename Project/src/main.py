from .database import SessionLocal, engine
from . import models

models.Base.metadata.create_all(bind=engine)
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "work code"}