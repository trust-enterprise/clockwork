
class Book():
    def __init__(self, book_name, author, year):
        self.book = book_name
        self.author = author
        self.year = year
        self.isIssued = False

library = []

while True:
    print("\n1. add book")
    print("2. view books")
    print("3. exit")

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
                status = f"{book.book} is available" if book.isIssued == False else f"{book.book} is unavailable"
                print(status)
    elif choice == "3":
        print(f"good bye!")
        break
    else:
        print("enter a valid option")
