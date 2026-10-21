from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.tasks import router as tasks_router
from app.db.base import Base
from app.db.session import engine
from app.models.task import Task  # noqa: F401 — регистрация таблицы в metadata

@asynccontextmanager
async def lifespan(app: FastAPI):
    # На лабораторной №3 создание таблиц будет заменено миграциями Alembic.
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title="Task Manager API", version="2.0.0", lifespan=lifespan)
app.include_router(tasks_router, prefix="/api/v1")
