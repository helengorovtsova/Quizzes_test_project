from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from environs import Env
import os

Base = declarative_base()

env = Env()
env.read_env()

db_host = os.getenv("POSTGRES_HOST")
db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")

DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}/{db_name}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_models():
    # Begin a transaction with the database engine
    async with engine.begin() as conn:
        # Create database tables using the metadata of the Base
        await conn.run_sync(Base.metadata.create_all)        

async def get_session() -> AsyncSession:
    # Create a new asynchronous session
    async with async_session() as session:
        yield session