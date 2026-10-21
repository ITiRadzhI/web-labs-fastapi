from fastapi import APIRouter, HTTPException, Response, status
from app.schemas.tasks import TaskCreate, TaskRead
from app.services import tasks as service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", response_model=list[TaskRead])
def get_tasks():
    return service.list_tasks()

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int):
    task = service.find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate):
    return service.create_task(data)

@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, data: TaskCreate):
    task = service.update_task(task_id, data)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if not service.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=204)
