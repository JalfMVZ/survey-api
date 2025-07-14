from app.schemas.base import BaseSchema
from typing import Optional, List
from datetime import datetime

class SurveyCreate(BaseSchema):
    title: str
    description: Optional[str] = None

class SurveyOut(BaseSchema):
    id: int
    title: str
    description: Optional[str] = None
    created_at: datetime
