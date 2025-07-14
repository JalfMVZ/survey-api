from app.schemas.base import BaseSchema
from typing import Optional, List
from datetime import datetime


from pydantic import Field, validator

class SurveyCreate(BaseSchema):
    title: str = Field(..., min_length=3, description="El título debe tener al menos 3 caracteres")
    description: Optional[str] = None

class SurveyOut(BaseSchema):
    id: int
    title: str
    description: Optional[str] = None
    created_at: datetime
