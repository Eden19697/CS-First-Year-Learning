"""
OOP + JSON Practice: Library Manager
====================================

Goal:
Build a small library management system that combines:

- class
- list of dictionaries
- auto-generated id
- search by id
- state update
- delete/filter
- keyword search
- JSON read/write


Book data format
----------------

Each book is a dictionary:

    {
        "id": 1,
        "title": "Python Basics",
        "author": "Alice Smith",
        "borrowed": False
    }

All books are stored in:

    self.books


Class
-----

Create:

    class LibraryManager


Methods
-------

1. add_book(title, author)

Add a new book.

Rules:
- id should be generated automatically.
- borrowed should start as False.
- return the new book dictionary.


2. borrow_book(book_id)

Borrow a book.

Rules:
- If the book exists and borrowed is False:
      set borrowed to True
      return True

- If the book does not exist or is already borrowed:
      return False


3. return_book(book_id)

Return a borrowed book.

Rules:
- If the book exists and borrowed is True:
      set borrowed to False
      return True

- If the book does not exist or is not borrowed:
      return False


4. delete_book(book_id)

Delete a book by id.

Rules:
- If deleted, return True.
- If not found, return False.


5. search_by_title(keyword)

Return all books whose title contains keyword.

For this exercise, search is case-sensitive.

Example:

    search_by_title("Python")

can match:

    "Python Basics"


6. list_available_books()

Return all books where borrowed is False.


7. save_to_file(filename)

Save books to a JSON file.


8. load_from_file(filename)

Load books from a JSON file and update next_id.


Expected output
---------------

True
False
True
False
[{'id': 1, 'title': 'Python Basics', 'author': 'Alice Smith', 'borrowed': False}]
[
    available books...
]
Wrote books to library.json
Loaded books from library.json
"""


import json


class LibraryManager:
    def __init__(self):
        # TODO: Create an empty books list.
        self.books = []

        # TODO: Create next_id starting from 1.
        self.next_id = 1

    def add_book(self, title, author):
        # TODO: Create a new book dictionary.
        book = {
            "id": self.next_id,
            "title": title,
            "author": author,
            "borrowed": False
        }
        # TODO: Append book to self.books.
        self.books.append(book)
        # TODO: Increase self.next_id.
        self.next_id += 1
        # TODO: Return the new book.
        return book

    def borrow_book(self, book_id):
        # TODO: Loop through books.
        for One_book in self.books:
        # TODO: If id matches and borrowed is False, set borrowed to True and return True.
            if One_book["id"] == book_id and One_book["borrowed"] == False:
                One_book["borrowed"] = True
                return True
        # TODO: Otherwise return False.
        return False

    def return_book(self, book_id):
        # TODO: Loop through books.
        for One_book in self.books:
        # TODO: If id matches and borrowed is True, set borrowed to False and return True.
            if One_book["id"] == book_id and One_book["borrowed"] == True:
                One_book["borrowed"] = False
                return True
        # TODO: Otherwise return False.
        return False

    def delete_book(self, book_id):
        # TODO: Loop through books by index.
        for index, book in enumerate(self.books):
        # TODO: If id matches, remove it and return True.
            if book["id"] == book_id:
                del self.books[index]
                return True
        # TODO: If not found, return False.
        return False

    def search_by_title(self, keyword):
        # TODO: Create results list.
        results = []
        # TODO: Add books whose title contains keyword.
        for One_book in self.books:
            if keyword in One_book["title"]:
                results.append(One_book)
        # TODO: Return results.
        return results

    def list_available_books(self):
        # TODO: Return books where borrowed is False.
        available = []
        for One_book in self.books:
            if not One_book["borrowed"]:
                available.append(One_book)
        return available

    def save_to_file(self, filename):
        # TODO: Open filename in write mode.
        with open(filename, "w") as file:
        # TODO: Save self.books using json.dump(..., indent=4).
            json.dump(self.books,file,indent=4)

    def load_from_file(self, filename):
        # TODO: Open filename in read mode.
        with open(filename, "r") as file:
        # TODO: Load books using json.load(file).
            new_file = json.load(file)
        # TODO: Update self.books.
            self.books = new_file
        # TODO: Update self.next_id so new books get a fresh id.
        if self.books:
            self.next_id = max(book["id"] for book in self.books) +1
        else:
            self.next_id = 1


def main():
    manager = LibraryManager()

    manager.add_book("Python Basics", "Alice Smith")
    manager.add_book("Clean Code", "Robert Martin")
    manager.add_book("Deep Learning", "Ian Goodfellow")

    print(manager.borrow_book(1))
    print(manager.borrow_book(1))

    print(manager.return_book(1))
    print(manager.return_book(1))

    print(manager.search_by_title("Python"))
    print(manager.list_available_books())

    manager.save_to_file("library.json")
    print("Wrote books to library.json")

    new_manager = LibraryManager()
    new_manager.load_from_file("library.json")
    print("Loaded books from library.json")
    print(new_manager.list_available_books())


if __name__ == "__main__":
    main()
