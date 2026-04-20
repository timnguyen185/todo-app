tasks = []

def add_task(task):
    tasks.append(task)

def list_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")