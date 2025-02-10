import sqlite3

conn = sqlite3.connect("tareas.db")
c = conn.cursor()
def create_table():
    with open("initdb.sql", "r") as f:
        c.executescript(f.read())
    conn.commit()

def add_task(title,status,desc=None):
    c.execute("INSERT INTO tasks(title,description,status) VALUES(?,?,?)",(title,desc,status))
    conn.commit()