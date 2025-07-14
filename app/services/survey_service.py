from app.models.survey import Survey
from app.schemas.survey import SurveyCreate
from sqlalchemy.orm import Session
from datetime import datetime

def create_survey(db: Session, survey_in: SurveyCreate):
    survey = Survey(title=survey_in.title, description=survey_in.description, created_at=datetime.utcnow())
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey
