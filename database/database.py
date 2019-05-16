import sqlite3

with sqlite3.connect('x-project.db') as db:
    c = db.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS user(
id INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
""")

c.execute("""
INSERT INTO user(username,password)
VALUES('admin','admin')
""")

db.commit()

c.execute("SELECT * FROM user")
print(c.fetchall())
