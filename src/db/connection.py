from sqlalchemy.ext.asyncio import create_async_engine
from src.config import CONFIG
from sqlalchemy import text
from src.db.models import Base, User

DB_URL = f"postgresql+asyncpg://{CONFIG.POSTGRES_USER}:{CONFIG.POSTGRES_PASSWORD}@db:5432/{CONFIG.POSTGRES_DB}"

engine = create_async_engine(
    url=DB_URL,
    echo=True
)

async def init_db():
    async with engine.begin() as conn:
        # statement = text("""SELECT 'Database Initialized'""")
        # result = await conn.execute(statement)
        # print("RESULT")
        # print(result.all())

        await conn.run_sync(Base.metadata.create_all)
        print("TABLE CREATED--------")