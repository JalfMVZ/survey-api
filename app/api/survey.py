from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.survey import SurveyCreate, SurveyOut
from app.schemas.question import QuestionCreate, QuestionOut
from app.schemas.option import OptionCreate, OptionOut
from app.services.survey_service import create_survey
from app.services.question_service import create_question
from app.services.option_service import create_option

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/surveys", response_model=SurveyOut, status_code=status.HTTP_201_CREATED)
def create_survey_endpoint(survey_in: SurveyCreate, db: Session = Depends(get_db)):
    return create_survey(db, survey_in)

@router.post("/surveys/{survey_id}/questions", response_model=QuestionOut, status_code=status.HTTP_201_CREATED)
def create_question_endpoint(survey_id: int, question_in: QuestionCreate, db: Session = Depends(get_db)):
    return create_question(db, survey_id, question_in)

@router.post("/questions/{question_id}/options", response_model=OptionOut, status_code=status.HTTP_201_CREATED)
def create_option_endpoint(question_id: int, option_in: OptionCreate, db: Session = Depends(get_db)):
    return create_option(db, question_id, option_in)
