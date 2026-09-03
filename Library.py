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
def StoreList(book):
    with open("Library.txt", "a") as file:
        file.write("{}, {}, {}\n".format(book[0], book[1], book[2])) 

def UpdateList():
    deletedlist = open("Library.txt", "w")
    for i in range(len(Library)):
        deletedlist.write("{}, {}, {}\n".format(Library[i][0], Library[i][1], Library[i][2]))
    deletedlist.close()

def Borrow_Or_Return():
    with open("Library.txt", "w") as editentry:
        for i in range(len(Library)):
            editentry.write("{}, {}, {}\n".format(Library[i][0], Library[i][1], Library[i][2]))

""" If the list is empty the checks are bypassed an the author is added to the database.
If it is not empty, the book is compared to previous entries to prevent duplicate entries """
def AddBook():
    query = input("What book would you like to add to the library?: ")
    found = False
    if len(Library) > 0:
        for i in range(len(Library)):
            title = Library[i][0]
            if query == title:
                print("Book is already in the library")
                found = True
                break
            elif found == False and i + 1 == len(Library):
                author = input("Who is the author of the book?: ")
                book = [query, author, "Available"]
                Library.append(book)
                StoreList(book)
    elif len(Library) == 0:
        author = input("Who is the author of the book?: ")
        book = [query, author, "Available"]
        Library.append(book)
        StoreList(book)

## Loads previous entries to fill list before the start of the program
def LoadLibrary():
    with open("Library.txt", "r") as FileLoad:
        for line in FileLoad:
            line = line.strip().split(", ")
            Library.append(line)

""" Searches through the library list. If book is found and available The user is allowed
to borrow. Any other condition prevents borrowing"""
def StatusChange(BorrowFlag, ReturnFlag):
    if userchoice == 2:
        query = input("What book do you want to borrow?: ")
    elif userchoice == 3:
        query = input("What book do you want to return?: ")
    found = False
    for borrow in range(len(Library)):
        title = Library[borrow][0]
        status = Library[borrow][2]
        if title == query and status == "Available" and BorrowFlag == True:
            Library[borrow][2] = "Borrowed"
            Borrow_Or_Return()
            found = True
            break
        elif title == query and status == "Borrowed" and ReturnFlag == True:
            Library[borrow][2] = "Available"
            Borrow_Or_Return()
            found = True
            break
        elif query == title and status == "Borrowed" and BorrowFlag == True:
            print("This book is already borrowed")
            break
        elif query == title and status == "Available" and ReturnFlag == True:
            print("This book is already available")       
            break
        elif borrow + 1 == len(Library) and found == False:
            print("Book not found")
            break

def ViewLibrary():
    ListNo = 0
    for i in range(len(Library)):
        ListNo += 1
        print("{}. {}, {}, {}".format(ListNo, Library[i][0], Library[i][1], Library[i][2]))

def Search_For_Book():
    found = False
    query = input("What book are you searching for?: ")
    for i in range(len(Library)):
        if query == Library[i][0]:
            print("{}, {}, {}".format(Library[i][0], Library[i][1], Library[i][2]))
            found == True
            break
        elif i + 1 == len(Library) and found == False:
            print("Book not found")

def DeleteBook():
    query = input("What book do you want to delete?: ")
    found = False
    for i in range(len(Library)):
        if query == Library[i][0]:
            Library.pop([i][0])
            found = True
            UpdateList()
            break
        elif i + 1 == len(Library) and found == False:
            print("Book not found")

Library = []
LoadLibrary()
userchoice = 0
while userchoice != 7:
    try:
        userchoice = LibraryMenu()
        if userchoice == 1:
            AddBook()
        elif userchoice == 2:
            StatusChange(True, False)
        elif userchoice == 3:
            StatusChange(False, True)
        elif userchoice == 4:
            ViewLibrary()
        elif userchoice == 5:
            Search_For_Book()
        elif userchoice == 6:
            DeleteBook()
    except ValueError:
        print("Invalid input")