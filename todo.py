def get_tasks(db):
    return [row[0] for row in db.execute("select task from tasks order by id")]


def add_task(db, task):
    db.execute("insert into tasks (task) values (%s)", (task,))
