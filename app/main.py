import contextlib

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy import select

from .database import create_all_tables, engine
from .models import Post


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def get():
    async with AsyncSession(engine) as session:
        result = await session.execute(select(Post))
        return result.scalars().all()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
