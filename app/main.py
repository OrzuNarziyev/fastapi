import contextlib

from fastapi import FastAPI

from app.database import create_all_tables, drop_all_tables


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_all_tables()
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
