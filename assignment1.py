"""
Name: Thomas Reaston
Date started: 30/03/2021
GitHub URL: cp1404-students/?????? <----- Fix this
"""

FILE_NAME = "books.csv"


# Menu function
def menu():
    user_menu_selection = str(input("Choose an item from the menu:-\n"
                                    "[L] - List all books available\n"
                                    "[A] - Add a book to the collection\n"
                                    "[C] - Mark a book as read\n"
                                    "[Q] - Quit the program\n"
                                    ":- "))
    user_menu_selection = user_menu_selection.upper()

    return user_menu_selection


# List books in book file
def list_books(input_file):
    print("List of available books")
    print("Books marked with an * have already been read")

    book_data = []
    line_count = 0
    input_file.seek(0)

    for line in input_file:
        line_count = line_count + 1
        line = line.strip()
        parts = line.split(',')
        book_name_data = parts[0]
        author_data = parts[1]
        number_of_pages_data = parts[2]
        read_or_unread = parts[3]
        if read_or_unread == "l":
            read_or_unread = "*"
            print("[{:2}]  {}  {:28} - {:22} ({}) ".format(line_count, read_or_unread, book_name_data, author_data,
                                                           number_of_pages_data))
        else:
            learned_or_complete = " "
            print("[{:2}]  {}  {:28} - {:22} ({}) ".format(line_count, read_or_unread, book_name_data, author_data,
                                                           number_of_pages_data))

        book_data.append(parts)

    return book_data
