__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"
#Practice dictionaries, sets, loops, and string methods.

library = {
    "Python101": "Available",
    "DataScience": "Available",
    "Algorithms": "Available"
}
menu = """
    1 - Add Book
    2 - Borrow Book
    3 - Return Book
    4 - View All Books
    5 - Exit
"""

borrowed_books = set()

def check_book_name(name, list):
    for book in list:
        if(name.lower() == book.lower()):
            return book
    return False

while(True):
    selection = input(menu)

    if selection.isdigit() and int(selection) in range(1,6):
        
        if selection == "1":
                new_book = input("Enter book name: ")

                library[new_book] = "Available"
        elif selection == "2":
            wanted_book = input("Enter book name: ")
            book_in_list = check_book_name(wanted_book, library)

            if book_in_list and (wanted_book.lower() not in borrowed_books):
                library[book_in_list] = 'Borrowed'

                borrowed_books.add(book_in_list.lower())
            elif(wanted_book.lower() in borrowed_books):
                print(f'{wanted_book} is not available wait for other user!')
            else:
                print(f'We have not {wanted_book}!')

        elif selection == "3":
            return_book = input("Enter book name: ")
            book_in_list = check_book_name(return_book, library)

            if book_in_list:
                library[book_in_list] = 'Available'

                borrowed_books.remove(book_in_list.lower())
            else:
                print(f'{return_book} is not saved our system!')

        elif selection == "4":
            for book in library:
                print(f"{book} is {library[book]}")

        elif selection == "5":
            break
        
    else:
        print("Enter nummer in menu!")