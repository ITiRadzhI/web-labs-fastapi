from app.schemas.tasks import TaskCreate, TaskRead

_tasks: dict[int, TaskRead] = {}
_next_id = 1


def list_tasks() -> list[TaskRead]:
    return list(_tasks.values())


def find_task(task_id: int) -> TaskRead | None:
    return _tasks.get(task_id)


def create_task(data: TaskCreate) -> TaskRead:
    global _next_id
    task = TaskRead(id=_next_id, **data.model_dump())
    _tasks[_next_id] = task
    _next_id += 1
    return task


def update_task(task_id: int, data: TaskCreate) -> TaskRead | None:
    if task_id not in _tasks:
        return None
    task = TaskRead(id=task_id, **data.model_dump())
    _tasks[task_id] = task
    return task


def delete_task(task_id: int) -> bool:
    return _tasks.pop(task_id, None) is not None
