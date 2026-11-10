from input import *



books = [
    {"id": 1, "name": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "available": True},
    {"id": 2, "name": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "available": True},
    {"id": 3, "name": "Clean Code", "author": "Robert Martin", "year": 2008, "available": False},
    {"id": 4, "name": "Atomic Habits","author": "James Clear", "year": 2018, "available": True},
    {"id": 5, "name": "The Pragmatic Programmer", "author": "David Thomas", "year": 1999, "available": False}
    ]



def main():
    escape = False
    while not escape:
        user_choice = input("""
        ================================
                LIBRARY MANAGEMENT
        ================================

        1. Display all books
        2. Search book by name
        3. Add new book
        4. Borrow a book
        5. Return a book
        6. Display available books
        7. Display books by author
        8. Exit
        Choose an option:
        """)

        if user_choice == "0":
            escape = True
        elif user_choice == "1":
            display_books(books)
        elif user_choice == "2":
            name = get_name()
            print(search_book(books, name))
        elif user_choice == "3":
            name = get_name()
            author = get_author()
            try:
                year = get_year()
            except ValueError as e:
                print(e)
            try:
                print(add_book(books, name, author, year))
            except ValueError as e:
                print(e)
        elif user_choice == "4":
            try:
                book_id = get_book_id()
                is_borrow = borrow_book(books, book_id)
                if is_borrow is False:
                    raise ValueError("Book Dont exists!")
                else:
                    print(is_borrow)
            except ValueError as e:
                print(e)
        
        elif user_choice == "5":
            try:
                book_id = get_book_id()
                print(return_book(books, book_id))
            except ValueError as e:
                print(e)
                
        elif user_choice == "6":
            try:
                print(get_available_books(books))
            except ValueError as e:
                print(e)
        elif user_choice == "7":
            try:
                author = get_author()
                print(get_books_by_author(books, author))
            except ValueError as e:
                print(e)
        


def get_next_book_id(books)->int:
    book_id = max(books, key= lambda i: i["id"]) 
    return book_id["id"] + 1


def display_books(books):
    for book in books:
        print(book)

def search_book(books, name):
    for book in books:
        if book["name"].lower() == name.lower():
            return book

def add_book(books, name, author, year):
    new_book = {}
    if not name or not author:
        raise ValueError("Name or author most be ")
    new_book["id"] = get_next_book_id(books)
    new_book["name"] = name
    new_book["author"] = author
    new_book["year"] = year
    for book in books:
        if book["name"] == new_book["name"] and book["author"] == new_book["author"]:
            raise ValueError("Book already exist")
    books.append(new_book)
    print(books)
    return new_book


def borrow_book(books, book_id):
    borrow_book = []
    for book in books:
        if book["id"] == book_id:
            if book["available"] == False:
                raise ValueError("Book not available")
            if book["available"] == True:
                borrow_book.append(book)
                book["available"] = False
            return borrow_book
    return False


def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"] == True:
                raise ValueError("book already exist")
            if book["available"] == False:
                book["available"] = True
                return True
    return False


def get_available_books(books):
    list_available = []
    for book in books:
        if book["available"] == True:
            list_available.append(book)
    if not list_available:
        raise ValueError("not available")
    return list_available



def get_books_by_author(books, author):
    book_by_author = []
    for book in books:
        if book["author"] == author:
            book_by_author.append(book)
    if not book_by_author:
        raise ValueError("Empty list")
    return book_by_author





if __name__ == "__main__":
    main()