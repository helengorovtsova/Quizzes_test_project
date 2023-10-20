from typing import Optional
from models.models import QuestionsInDB, QuestionsRequest
from db.base import get_session, init_models
from fastapi import FastAPI
from services.services import add_questions, get_questions
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
import typer
import asyncio

app = FastAPI()

cli = typer.Typer()

# Command to initialize the database
@cli.command()
def db_init_models() -> None:
    asyncio.run(init_models())
    print("Done")

if __name__ == "__main__":
    cli()

# Endpoints for the API: POST-request
@app.post("/questions")
async def add_new_questions(
    questions_request: QuestionsRequest,
    session: AsyncSession = Depends(get_session)
) -> Optional[QuestionsInDB]:
    
    question = await add_questions(
        session=session, 
        questions_num=questions_request.questions_num
    )
    
    try:
        await session.commit()
        if question:
            return question[-1]
        else:
            return None
    except Exception as e:
        await session.rollback()
        raise e
    
# Endpoints for the API: GET-request
@app.get("/questions/{question_id}", response_model=Optional[QuestionsInDB])
async def get_question_by_id(
    question_id: int, 
    session: AsyncSession = Depends(get_session)
):
    
    question = await get_questions(session, question_id=question_id)
    if question is None:
        return None
    else:
        return question
