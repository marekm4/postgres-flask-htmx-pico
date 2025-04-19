tasks = [
    "Install Pico CSS",
    "Install htmx",
    "Install Flask",
    "Install PostgreSQL",
]


def get_tasks():
    return tasks


def add_task(task):
    tasks.append(task)
