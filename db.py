import os

import psycopg


def get_db():
    db = psycopg.Connection.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME"),
    )
    db.autocommit = True
    db.row_factory = psycopg.rows.dict_row
    return db


def get_users(db):
    return [row["name"] for row in db.execute("select name from users order by id")]


def add_user(db, name):
    db.execute("insert into users (name) values (%s)", (name,))
