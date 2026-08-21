library = []
def menu():
    print("1. Add book\n2. Borrow book\n3. Return book\n4. View all books\n5. Search for book\n6. Delete a book\n7. Save and exit")
    userchoice = int(input("Pick an option: "))
    return userchoice
def ADD_BOOK():
    title = input("What is the title of the book?: ").title()
    if len(library) > 0:
        for check in range(len(library)):
            i0 = library[check][0]
            if i0 == title:
                print("Book is already in the library")
                break
            elif i0 != title and check + 1 == len(library):
                author = input("Who is the author of the book?: ").upper()
                library.append([title, author, "Available"])
                library.sort()
                books = open("Books.txt", "w")
                for i in range(len(library)):
                    books.write("{}, {}, {}\n".format(library[i][0], library[i][1], library[i][2]))
                books.close()
                break
    else:
        author = input("Who is the author of the book?: ").upper()
        library.append([title, author, "Available"])
        library.sort()
        books = open("Books.txt", "w")
        for i in range(len(library)):
            books.write("{}, {}, {}\n".format(library[i][0], library[i][1], library[i][2]))
        books.close()
def BORROW_BOOK():
    borrow = input("What book do you want to borrow?: ").title()
    for index in range(len(library)):
        i0 = library[index][0]
        i1 = library[index][1]
        i2 = library[index][2]
        if i0 == borrow and i2 == "Available":
            library[index][2] = "Borrowed"
            books = open("Books.txt", "w")
            for i in range(len(library)):
                books.write("{}, {}, {}\n".format(library[i][0], library[i][1], library[i][2]))
            books.close()
            break
        elif i0 == borrow and i2 == "Borrowed":
            print("Book is already borrowed")
def RETURN_BOOK():
    returns = input("What book are you returning?: ").title()
    for index in range(len(library)):
        i0 = library[index][0]
        i1 = library[index][1]
        i2 = library[index][2]
        if i0 == returns and i2 == "Borrowed":
            library[index][2] = "Available"
            books = open("Books.txt", "w")
            for i in range(len(library)):
                books.write("{}, {}, {}\n".format(library[i][0], library[i][1], library[i][2]))
            books.close()
            break
        elif i0 == returns and i2 == "Available":
            print("This book was not borrowed")
def VIEW_BOOKS():
    header = "Library list".center(105)
    print(header)
    listno = 0
    for i in range(len(library)):
        listno += 1
        i0 = library[i][0]
        i1 = library[i][1]
        i2 = library[i][2]
        print("{}. Title: {}\n   Author: {}\n   Status: {}\n".format(listno, i0, i1, i2))
def SEARCH_BOOKS():
    search = input("What book do you want to find?: ").title()
    for i in range(len(library)):
        i0 = library[i][0]
        i1 = library[i][1]
        i2 = library[i][2]
        if i0 == search:
            print("Title: {}\nAuthor: {}\nStatus: {}".format(i0, i1, i2))
            break
        elif i0 != search and i == len(library) - 1:
            print("Book not found")
def DELETE_BOOK():
    delete = input("What book do you want to delete?: ").title()
    for index in range(len(library)):
        i0 = library[index][0]
        if delete == i0:
            library.pop(index)
            books = open("Books.txt", "w")
            for i in range(len(library)):
                books.write("{}, {}, {}\n".format(library[i][0], library[i][1], library[i][2]))
            books.close()
            break
        elif delete != i0 and index == len(library) - 1:
            print("This book does not exist")
def COUNT_BOOKS():
    bookCount = 0
    Astat = 0
    Bstat = 0
    for count in range(len(library)):
        bookCount += 1
        i0 = library[count][0]
        i2 = library[count][2]
        if i2 == "Available":
            Astat += 1
        elif i2 == "Borrowed":
            Bstat += 1
    print("\nLibrary Summary\n------------\nTotal books: {}\nAvailable: {}\nBorrowed: {}\n".format(bookCount, Astat, Bstat))
userchoice = 0
while userchoice != 7:
    try:
        COUNT_BOOKS()
        userchoice = menu()
        if userchoice == 1:
            ADD_BOOK()
        elif userchoice == 2:
            BORROW_BOOK()
        elif userchoice == 3:
            RETURN_BOOK()
        elif userchoice == 4:
            VIEW_BOOKS()
        elif userchoice == 5:
            SEARCH_BOOKS()
        elif userchoice == 6:
            DELETE_BOOK()
    except ValueError:
        print("Choose a number between 1 and 7")