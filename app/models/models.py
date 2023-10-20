from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db.base import Base


class Questions(Base):
    # Defining a SQLAlchemy model for the "questions" table
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    text = Column(String)
    answer = Column(String)
    created_at = Column(String)


class QuestionsInDB(BaseModel):
    # Defining a Pydantic model for querying questions in the database
    text: str
    answer: str
    created_at: str

class QuestionsRequest(BaseModel):
    # Defining a Pydantic model for incoming requests with "questions_num" field
    questions_num: int