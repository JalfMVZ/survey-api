from app.schemas.base import BaseSchema
from typing import Optional, List
from enum import Enum

class QuestionType(str, Enum):
    text = "text"
    single_choice = "single_choice"
    multiple_choice = "multiple_choice"


from pydantic import Field
from typing import Literal

class QuestionCreate(BaseSchema):
    text: str = Field(..., min_length=1, description="El texto de la pregunta no puede estar vacío")
    question_type: QuestionType

class QuestionOut(BaseSchema):
    id: int
    text: str
    question_type: QuestionType
    survey_id: int
