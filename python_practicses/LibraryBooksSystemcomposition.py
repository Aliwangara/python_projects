# Requirements
# Class: Book

# Private Attributes:

# __title

# __author

# Methods:

# __init__(self, title, author)

# book_info(self) → prints: "Book: <title> by <author>"

# Class: Library

# Private Attributes:

# __name

# __books → list of Book objects

# Methods:

# __init__(self, name) → initializes library name and empty book list

# add_book(self, book) → adds a new book to the library

# show_books(self) → prints all books using each book’s book_info()

# total_books(self) → prints: "Total books: X"

# 📗 Program Flow

# Create a library named "City Library".

# Create three books:

# "Python Crash Course" by Eric Matthes

# "Clean Code" by Robert C. Martin

# "Atomic Habits" by James Clear

# Add the books to the library.

# Display all books and total count.


class Book:
    def __init__(self,title, author):
        self.__title  = title
        self.__author = author

    def get_author(self):
        return self.__author
    def get_title(self):
        return self.__title
    def book_info(self):
        print(f"Book: {self.__title}, By: {self.__author}")

class Library:
    def __init__(self,name):
       self.__name = name
       self.__books = []
    def add_books(self,book):
        self.__books.append(book)
    def show_books(self):
        print(f"\nLibrary {self.__name}")
        for i in self.__books:
            i.book_info()
    def total_books(self):
        print(f"Total Books: {len(self.__books)}")

book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Clean Code","Robert C. Martin" )
book3 = Book("Atomic Habits", "James Clear")


library = Library("City Library")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

library.show_books()
library.total_books()










