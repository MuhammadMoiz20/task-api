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
