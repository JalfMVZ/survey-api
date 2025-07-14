from app.models.option import Option
from app.models.question import Question, QuestionType
from app.schemas.option import OptionCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def create_option(db: Session, question_id: int, option_in: OptionCreate):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if question.question_type not in [QuestionType.single_choice, QuestionType.multiple_choice]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se pueden agregar opciones a preguntas de tipo single_choice o multiple_choice"
        )
    option = Option(text=option_in.text, question_id=question_id)
    db.add(option)
    db.commit()
    db.refresh(option)
    return option
