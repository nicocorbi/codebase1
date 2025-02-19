import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()
def create_table():
    with open("users.sql", "r") as f:
        c.executescript(f.read())
    conn.commit()

def add_task(name,gender,desc=None):
    c.execute("INSERT INTO tasks(username,password) VALUES(?,?,?)",(name,desc,gender))
    conn.commit()

