"""
Name: Thomas Reaston
Date started: 30/03/2021
GitHub URL: cp1404-students/a1-ThomasReaston <----- Fix this
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

