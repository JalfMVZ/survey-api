from app.schemas.base import BaseSchema


from pydantic import Field, validator

class OptionCreate(BaseSchema):
    text: str = Field(..., min_length=1, description="El texto de la opción no puede estar vacío")

class OptionOut(BaseSchema):
    id: int
    text: str
    question_id: int
