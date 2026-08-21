## Displays the menu to provide options for the user
def LibraryMenu():
    print("Choose an option (enter a number from 1-7)")
    print("1. Add book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. View all books")
    print("5. Search for a book")
    print("6. Delete book")
    print("7. Exit")
    userchoice = int(input(" "))
    return userchoice

##Stores the library list in a txt file
def StoreList():
    ListUpdate = open("Library.txt", "w")
    for entry in range(len(Library)):
        title = Library[entry][0]
        author = Library[entry][1]
        status = Library[entry][2]
        ListUpdate.write("{}, {}, {}\n".format(title, author, status))
    ListUpdate.close()

""" If the list is empty the checks are bypassed an the author is added to the database.
If it is not empty, the book is compared to previous entries to prevent duplicate entries """
def AddBook():
    query = input("What book would you like to add to the library?: ")
    found = False
    if len(Library) > 0:
        for i in range(len(Library)):
            book = Library[i][0]
            if query == book:
                print("Book is already in the library")
                found = True
                break
            elif found == False and i + 1 == len(Library):
                author = input("Who is the author of the book?: ")
                Library.append([query, author, "Available"])
                StoreList()
    elif len(Library) == 0:
        author = input("Who is the author of the book?: ")
        Library.append([query, author, "Available"])
        StoreList()

""" Searches through the library list. If book is found and available The user is allowed
to borrow. Any other condition prevents borrowing"""
def BorrowBook():
    query = input("What book do yu want to borrow?: ")
    found = False
    for borrow in range(len(Library)):
        book = Library[borrow][0]
        status = Library[borrow][2]
        if book == query and status == "Available":
            Library[borrow][2] = "Borrowed"
            found = True
            break
        elif borrow == len(Library) and found == False:
            print("Book not found")
        elif query == book and status == "Borrowed":
            print("This book is already borrowed")

Library = []
userchoice = 0
while userchoice != 7:
    try:
        userchoice = LibraryMenu()
        if userchoice == 1:
            AddBook()
    except ValueError:
        print("Invalid input")