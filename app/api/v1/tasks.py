from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.schemas.tasks import TaskCreate, TaskRead
from app.services import tasks as service

router = APIRouter(prefix="/tasks", tags=["Tasks"])
Session = Annotated[AsyncSession, Depends(get_session)]

@router.get("", response_model=list[TaskRead])
async def get_tasks(session: Session):
    return await service.list_tasks(session)

@router.get("/{task_id}", response_model=TaskRead)
async def get_task(task_id: int, session: Session):
    task = await service.find_task(session, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(data: TaskCreate, session: Session):
    return await service.create_task(session, data)

@router.put("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int, data: TaskCreate, session: Session):
    task = await service.update_task(session, task_id, data)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, session: Session):
    if not await service.delete_task(session, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=204)
