

def get_name():
    escape_name_found = False
    while not escape_name_found:
        input_name = input("Enter name: ").strip()
        if input_name != "":
            escape_name_found=True
            return input_name


def get_year():
    escape_year_found = False
    while not escape_year_found:
        input_year = int(input("Enter year: "))
        if input_year > 0:
            escape_year_found=True
            return input_year


def get_author():
    escape_author_found = False
    while not escape_author_found:
        input_author = input("Enter author: ").strip()
        if input_author != "":
            escape_author_found=True
            return input_author
        


def get_book_id():
    escape_book_id_found = False
    while not escape_book_id_found:
        book_id = int(input("Enter Book ID: "))
        if book_id > 0:
            return book_id
            