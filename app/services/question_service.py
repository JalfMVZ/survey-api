from app.models.question import Question, QuestionType
from app.models.survey import Survey
from app.schemas.question import QuestionCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def create_question(db: Session, survey_id: int, question_in: QuestionCreate):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    question = Question(text=question_in.text, question_type=question_in.question_type, survey_id=survey_id)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question
