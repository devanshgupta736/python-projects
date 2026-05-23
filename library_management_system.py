books = []

while True:
    print("Library Management System")
    print("1 . Add Book")
    print("2 . Show Books")
    print("3 . Search Book")
    print("4 . Remove Book")
    print("5 . Exit...")

    choice = input("Enter Choice (1 - 5) : ")

    if choice == "1":
        name = input("Enter Book Name : ")
        author = input("Enter Author Name : ")

        book = {
            "book_name" : name,
            "author" : author
        }

        books.append(book)
        print("Books Added Successfully")
    
    elif choice == "2":
        if len(books) == 0:
            print("No Books Found") 
        else:
            for i in books:
                print(i)
    
    elif choice == "3":
        search_book = input("Enter Book For Search : ")

        for i in books:
            if i["book_name"] == search_book:
                print("Book Found")
                print(i)

    elif choice == "4":
        remove_book = input("Enter the Book For Remove : ")

        for i in books:
            if i["book_name"] == remove_book:
                books.remove(i)
                print("Book Removed Successfully")

    elif choice == "5":
        print("Exit...")
        break

    else:
        print("Invalid Move")


