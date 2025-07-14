from app.schemas.base import BaseSchema

class OptionCreate(BaseSchema):
    text: str

class OptionOut(BaseSchema):
    id: int
    text: str
    question_id: int
