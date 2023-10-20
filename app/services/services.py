from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Questions
from sqlalchemy import select
import httpx

QUIZES_URL = "https://jservice.io/api/random?count="

async def add_questions(
        session: AsyncSession, 
        questions_num: int
    ) -> list[Questions]:

    async with httpx.AsyncClient() as client:
        response = await client.get(QUIZES_URL + str(questions_num))

    if response.status_code == 200:
        questions = response.json()
    else:
        raise Exception("Error while getting questions from API")
    
    question_objects = []

    for question in questions:
        # Check if the question already exists in the database
        existing_question = await session.execute(select(Questions).filter_by(id=question["id"]))
        if not existing_question.scalars().first():
            # Create a new Questions object and add it to the session
            question_obj = Questions(
                id=question["id"],
                text=question["question"],
                answer=question["answer"],
                created_at=question["created_at"]
            )    
            session.add(question_obj)
            question_objects.append(question_obj)
        else:
            continue
    return question_objects


async def get_questions(session: AsyncSession, question_id: int) -> Questions:
    result = await session.execute(select(Questions).where(Questions.id == question_id))
    result = result.scalars().first()    
    return result