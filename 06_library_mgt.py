
class Book():
    def __init__(self, book_name, author):
        self.title = book_name
        self.author = author 
        self.isIssued = False
    
    def issue(self, issuer):
        if self.isIssued:
            print(f"{self.title} is already issued")
        else:
            print(f"{self.title} is issued successfully by {issuer}")
            self.isIssued = True
    
    def return_book(self):
        if self.isIssued:
            print(f"{self.title} is returned successfully")
            self.isIssued = False
        else:
            print(f"{self.title} is returned already")

library = []

while True:
    print("\n1. add book")
    print("2. view books")
    print("3. issue book")
    print("4. return book")
    print("5. exit")

    choice = input("enter a number: ")

    if choice == "1":
        book_name = input("enter book's name: ")
        author = input("enter author's name: ") 
        book = Book(book_name, author)
        library.append(book)
        print(f"Book {book_name} has been added")
    elif choice == "2":
        if not library:
            print(f"there are no books available") 
        else:
            for book in library:
                status = "available" if book.isIssued == False else "issued"
                print(f"{book.title} by {book.author} is {status}")
    elif choice == "3":
        title = input("enter book title you want to get issued: ")

        for book in library:
            if book.title == title:
                issuer = input("issued by: ")
                book.issue(issuer)
                break
        else:
            print(f"{title} book not found for issue")
    elif choice == "4":
        title = input("enter the book title you wish to return: ")

        for book in library:
            if book.title == title: 
                book.return_book()
                break
        else:
            print(f"{title} book not found for return")
    elif choice == "5":
        print(f"good bye!")
        break
    else:
        print("enter a valid option")
