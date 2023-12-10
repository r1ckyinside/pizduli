import sqlite3


def contacts():
    con = sqlite3.connect("users.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users


print(contacts())

