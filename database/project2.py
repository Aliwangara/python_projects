import sqlite3

conn = sqlite3.connect('project2.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS project2(
               name TEXT NOT NULL,
               email TEXT PRIMARY KEY,
               age INTEGER ,
               marks BLOB DEFAULT 'unknown'
               
               
               
               )




''')

cursor.execute("INSERT INTO project2(name,email,age) VALUES(?,?,?)", ("ali","aliwangara63@gmail.com",22))


cursor.execute("SELECT * FROM project2")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()