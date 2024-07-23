library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


def add_book(library):
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


    title = input("Whats the book Title: ")
    author = input("Whats the Authors name: ")
    new_entry = [title, author]
    

    if new_entry in library:
        print(f"The book '{title}' by {author} is already in the library.")
    else:
        library.append(new_entry)
        print(f"The book '{title}' by {author} has been added to the library.")
        print(library)

def display_library(library):
    if not library:
        print("The library is empty.")
    else:
        print("\nLibrary Contents:")
        for i, book in enumerate(library, 1):
            title, author = book
            print(f"Book {i}: Title: {title}, Author: {author}")
            print(library)
            
    

def start_menu():
    while True:
        print("\nWelcome to the Library Application\n")
        print("Menu: ")
        print("1. Add Books")
        print("2. View Books")
        print("3. Exit")

        selection = input("Please enter your option (1-3): ")
        if selection == "1":
            add_book(library)
        elif selection == "2":
            display_library(library)
        elif selection == "3":
            break
        else:
            print("Please enter a valid selection.")
   
start_menu()