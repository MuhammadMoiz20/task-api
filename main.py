tasks = []
@app.get('/tasks', response_model=list[Task])
def get_tasks():
    return tasks
@app.post('/tasks', response_model=Task)
def create_task(task: TaskCreate):
    task_id = len(tasks) + 1
    new_task = Task(id=task_id, title=task.title)
    tasks.append(new_task)
    return new_task
@app.put('/tasks/{task_id}', response_model=Task)
def update_task(task_id: int, task: TaskCreate):
    for t in tasks:
        if t.id == task_id:
            t.title = task.title
            return t
    raise HTTPException(status_code=404, detail='Task not found')
