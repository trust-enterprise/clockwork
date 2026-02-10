
class Book():
    def __init__(self, book_name, author, year):
        self.book = book_name
        self.author = author
        self.year = year
        self.isIssued = False
    
    def issue(self):
        if self.isIssued:
            print(f"{self.book} is already issued")
        else:
            print(f"{self.book} is issued successfully")
            self.isIssued = True
    
    def return_book(self):
        if not self.isIssued:
            print(f"{self.book} is returned successfully")
            self.isIssued = False
        else:
            print(f"{self.book} is returned already")

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
        year = input("year of publishing: ")
        book = Book(book_name, author, year)
        library.append(book)
        print(f"Book {book_name} has been added")
    elif choice == "2":
        if not library:
            print(f"there are no books available") 
        else:
            for book in library:
                status = "available" if book.isIssued == False else "issued"
                print(f"{book.book} by {book.author} ({book.year}) is {status}")
    elif choice == "3":
        title = input("enter book title you want to get issued: ")

        for book in library:
            if book.book == title:
                book.issue()
                
            else:
                print("book not found")
    elif choice == "4":
        title = input("enter the book title you wish to return: ")

        for book in library:
            if book.book == title:
                book.return_book()
            else:
                print("book not found")
    elif choice == "5":
        print(f"good bye!")
        break
    else:
        print("enter a valid option")
