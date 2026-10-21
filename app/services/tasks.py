from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task import Task
from app.schemas.tasks import TaskCreate

async def list_tasks(session: AsyncSession) -> list[Task]:
    result = await session.scalars(select(Task).order_by(Task.id))
    return list(result.all())

async def find_task(session: AsyncSession, task_id: int) -> Task | None:
    return await session.get(Task, task_id)

async def create_task(session: AsyncSession, data: TaskCreate) -> Task:
    task = Task(**data.model_dump())
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

async def update_task(session: AsyncSession, task_id: int, data: TaskCreate) -> Task | None:
    task = await session.get(Task, task_id)
    if task is None:
        return None
    for key, value in data.model_dump().items():
        setattr(task, key, value)
    await session.commit()
    await session.refresh(task)
    return task

async def delete_task(session: AsyncSession, task_id: int) -> bool:
    task = await session.get(Task, task_id)
    if task is None:
        return False
    await session.delete(task)
    await session.commit()
    return True
