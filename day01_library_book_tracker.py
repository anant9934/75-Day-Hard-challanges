"""
Library Book Tracker
A very simple Python project using only strings, tuples, dictionaries, and lists.

Features:
- Add a book
- View all books
- Borrow a book
- Return a book

Author: ANANT KUMAR
Date: 26-10-2025
"""

# This list will store all your books
library_inventory = []

# Add a new book
def add_book(title, author, year):
    # Create a book dictionary with title, tuple of (author, year), and status info
    book = {
        "title": title,
        "author_info": (author, year),
        "status": {"available": True, "borrowed_by": None}
    }
    library_inventory.append(book)
    print(f"Book '{title}' added!")

# Show all books
def view_books():
    if not library_inventory:
        print("No books in the library.\n")
    else:
        print("\n-- Library Books --")
        for book in library_inventory:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author_info'][0]}")
            print(f"Year: {book['author_info'][1]}")
            print(f"Available: {book['status']['available']}")
            print(f"Borrowed By: {book['status']['borrowed_by']}\n")

# Borrow a book by title
def borrow_book(title, user):
    for book in library_inventory:
        if book["title"].lower() == title.lower():
            if book["status"]["available"]:
                book["status"]["available"] = False
                book["status"]["borrowed_by"] = user
                print(f"{user} borrowed '{title}'.")
                return
            else:
                print(f"'{title}' is already borrowed by {book['status']['borrowed_by']}.")
                return
    print(f"No book found with the title '{title}'.")

# Return a book by title
def return_book(title):
    for book in library_inventory:
        if book["title"].lower() == title.lower():
            if not book["status"]["available"]:
                print(f"Book '{title}' returned.")
                book["status"]["available"] = True
                book["status"]["borrowed_by"] = None
                return
            else:
                print(f"'{title}' was not borrowed.")
                return
    print(f"No book found with the title '{title}'.")

# Main menu for user interaction
def menu():
    print("\n--- Library Book Tracker ---")
    print("1. Add a Book")
    print("2. View all Books")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit")

# Main program loop
if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            year = input("Publication Year: ")
            add_book(title, author, year)
        elif choice == "2":
            view_books()
        elif choice == "3":
            title = input("Book Title to Borrow: ")
            user = input("Your Name: ")
            borrow_book(title, user)
        elif choice == "4":
            title = input("Book Title to Return: ")
            return_book(title)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
