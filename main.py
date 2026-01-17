from fastapi import FastAPI
from src.db.connection import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server is stopping...")

app = FastAPI(
    lifespan=lifespan
)

@app.get("/")
def main():
    return {"message": "Hello World"}
