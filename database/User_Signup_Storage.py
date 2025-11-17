import sqlite3
import datetime
today = datetime.date.today()

conn = sqlite3.connect("signup.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS signup(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL,
               signup_date TEXT DEFAULT CURRENT_DATE
                     
               )

''')

# cursor.execute("INSERT INTO signup(username,email,password,signup_date) VALUES(?,?,?,?)", ("Ali","aliwangara@gmail.com","123456","15-7-2022"))
cursor.execute("INSERT INTO signup(username,email,password) VALUES(?,?,?)", ("George","alig@gmail.com","123456"))
 
cursor.execute('''
  UPDATE signup
  SET password = 'ali'
  WHERE email = 'aliwangara@gmail.com'


''')

# cursor.execute('''
#     DELETE FROM signup
#     WHERE email = 'alig@gmail.com'


# ''')


cursor.execute("SELECT * FROM signup")

rows = cursor.fetchall()

for row in rows:
    print(row)







conn.commit()
conn.close()


# Update a user’s password

# Find a user by their email.

# Change their password to a new one of your choice.

# Print all users to confirm the change.



