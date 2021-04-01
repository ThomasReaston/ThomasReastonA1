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
                                    "[R] - Mark a book as read\n"
                                    "[Q] - Quit the program\n"
                                    ":- "))
    user_menu_selection = user_menu_selection.upper()

    return user_menu_selection


# List books in book file
def list_books(input_file):
    print("List of available books")
    print("Books marked with an c have already been completed")

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
        if read_or_unread == "c":
            read_or_unread = "r"
            print("[{:2}]  {}  {:28} by {:22} ({}) ".format(line_count, read_or_unread, book_name_data, author_data,
                                                           number_of_pages_data))
        else:
            read_or_unread = "c"
            print("[{:2}]  {}  {:28} by {:22} ({}) ".format(line_count, read_or_unread, book_name_data, author_data,
                                                           number_of_pages_data))

        book_data.append(parts)

    return book_data


# Add books to list - Default is unread or r
def add_books(output_file):
    print("Add a book to the collection")

    book_title = str(input("Enter the books name:- "))
    author_name = str(input("Enter the author name:- "))
    number_of_pages = int(input("Enter the number of pages:- "))
    book_input = "{},{},{}".format(book_title.title(), author_name.title(), number_of_pages)
    output_file.write("\n{},r\n".format(book_input))
    print("Book added successfully")


# Change books to read 'r' and write over file
def mark_as_read(input_file, output_file):
    list_books(input_file)

    try:
        book_selection = int(input("Which book do you want to mark as read? [#]\n"))

    except ValueError:
        print("Choice must be a number")
        book_selection = int(input("Which book do you want to mark as read? [#]\n"))

    input_file.seek(0)

    lines = input_file.readlines()
    book_selection = book_selection - 1

    book_to_change = str(lines[book_selection])

    book_to_change = book_to_change.replace("c", "r")

    lines[book_selection] = book_to_change

    output_file = open(FILE_NAME, 'w')
    # Overwrite file with book changed to read

    output_file.writelines(lines)

    output_file.close()

    print("Book changed to read\n")


def main():
    print("Welcome to the Reading Tracker Program - by Thomas Reaston")

    input_file = open(FILE_NAME, 'r')
    output_file = open(FILE_NAME, 'a')

    user_menu_selection = menu()

    while len(user_menu_selection) != 1:
        print("You must only enter 1 character as your choice - Try again")
        user_menu_selection = menu()

    while user_menu_selection.isalpha() is False:
        print("You must enter a letter as your choice - Try again")
        user_menu_selection = menu()

    while user_menu_selection != "Q":

        if user_menu_selection == "L":
            book_data = list_books(input_file)
            print("")

        elif user_menu_selection == "A":
            add_books(output_file)
            print("")

        elif user_menu_selection == "R":
            mark_as_read(input_file, output_file)

        else:
            print("Not a valid menu option - Try again")

        user_menu_selection = menu()

    print("Good-bye. Thank you for using this program")

    input_file.close()
    output_file.close()


main()
