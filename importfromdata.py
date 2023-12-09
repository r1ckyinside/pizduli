import sqlite3

con = sqlite3.connect("data.sqlite3")
cursor = con.cursor()
cursor.execute("SELECT * FROM meme")
meme = cursor.fetchall()

