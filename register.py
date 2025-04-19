def get_users(db):
    return [row[0] for row in db.execute("select name from users order by id")]


def add_user(db, name):
    db.execute("insert into users (name) values (%s)", (name,))
