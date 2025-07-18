from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class QuestionType(enum.Enum):
    text = "text"
    single_choice = "single_choice"
    multiple_choice = "multiple_choice"

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    question_type = Column(Enum(QuestionType), nullable=False)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    survey = relationship("Survey", back_populates="questions")
    options = relationship("Option", back_populates="question", cascade="all, delete-orphan")
