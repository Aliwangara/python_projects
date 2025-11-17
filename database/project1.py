import sqlite3

conn = sqlite3.connect('project1.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS project(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT)

''')

conn.commit()

conn.close()


# CREATE TABLE IF NOT EXISTS

# Purpose: Creates a new table in the database, but only if it doesn’t already exist.

# Syntax:

# CREATE TABLE IF NOT EXISTS table_name (
#     column1 datatype constraints,
#     column2 datatype constraints,
#     ...
# );


# Example:

# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER,
#     grade TEXT
# );


# Explanation:

# CREATE TABLE → make a table.

# IF NOT EXISTS → prevents an error if the table already exists.

# students → name of the table.

# 2. Data Types

# SQLite uses dynamic typing, but these are the common ones:

# Type	Description
# INTEGER	Whole numbers. Can also be PRIMARY KEY for unique IDs.
# REAL	Floating-point numbers (decimals).
# TEXT	Text or string data (names, descriptions).
# BLOB	Binary data (images, files).
# NUMERIC	Numbers stored as integers, floats, or strings (depending on usage).
# 3. PRIMARY KEY

# Purpose: Uniquely identifies each row in a table.

# Example: id INTEGER PRIMARY KEY

# Tip: Each table should have a primary key for unique identification.

# 4. AUTOINCREMENT

# Purpose: Automatically increases the value of the primary key for each new row.

# Example:

# id INTEGER PRIMARY KEY AUTOINCREMENT


# If your first row has id=1, the next row inserted will automatically get id=2, then 3, etc.

# 5. Other constraints

# NOT NULL → column must have a value (cannot be empty).

# UNIQUE → ensures all values in that column are unique.

# DEFAULT value → assigns a default value if no value is given.

# 6. Putting it together
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     grade TEXT DEFAULT 'Unknown'
# );


# Creates a students table if it doesn’t exist.

# id auto-increments.

# name must be provided.

# grade defaults to 'Unknown' if not specified.


# Exercise 1: Creating and Populating a Table
# Task:

# Create a table called books with the following columns:

# id → INTEGER, PRIMARY KEY, AUTOINCREMENT

# title → TEXT, NOT NULL

# author → TEXT, NOT NULL

# year_published → INTEGER

# genre → TEXT, default value "Unknown"

# Insert at least 3 books into the table with your choice of values.

# After inserting, retrieve all rows from the table and print them.


conn = sqlite3.connect('books.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year_published INTEGER,
        genre TEXT DEFAULT 'Unknown'
    )
''')

cursor.execute("INSERT INTO books (title, author, year_published, genre) VALUES (?, ?, ?, ?)",
               ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy"))
cursor.execute("INSERT INTO books (title, author, year_published, genre) VALUES (?, ?, ?, ?)",
               ("1984", "George Orwell", 1949, "Dystopian"))
cursor.execute("INSERT INTO books (title, author, year_published) VALUES (?, ?, ?)",
               ("To Kill a Mockingbird", "Harper Lee", 1960))

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()














