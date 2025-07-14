from app.schemas.base import BaseSchema
from typing import Optional, List
from enum import Enum

class QuestionType(str, Enum):
    text = "text"
    single_choice = "single_choice"
    multiple_choice = "multiple_choice"

class QuestionCreate(BaseSchema):
    text: str
    question_type: QuestionType

class QuestionOut(BaseSchema):
    id: int
    text: str
    question_type: QuestionType
    survey_id: int
