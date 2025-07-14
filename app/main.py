from fastapi import FastAPI
from app.api import survey

app = FastAPI()

app.include_router(survey.router)
