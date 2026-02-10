import requests
class Book():
    def __init__(self, book_name, author):
        self.title = book_name
        self.author = author 
        self.isIssued = False
        self.reviews = []
        self.summarize_reviews = None
    
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

    def summarize_reviews(self):
        url = "https://api.example.com/summarize"

        payload = {
            "text": " ".join(self.reviews)
        }

        response = requests.post(url, json = payload)

        if response.status_code == 200:
            data = response.json()
            return data.get("summary", "summary not available")
        else:
            return "failed to summarize reviews"
        # review_length = 0

        # for review in self.reviews:
        #     review_length += len(review)
        
        # avg_review_length = review_length / len(self.reviews)

        # if avg_review_length < 20:
        #     print(f"{book.title} has mixed reviews")
        # else:
        #     print(f"{book.title} has mixed reviews") 

library = []

while True:
    print("\n1. add book")
    print("2. view books")
    print("3. issue book")
    print("4. return book")
    print("5. add review")
    print("6. summarize reviews")
    print("7. exit")

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
    elif choice == "5": #add review
        title = input("enter book you want to review: ")
        
        for book in library:
            if book.title == title:
                review = input("enter your review: ")
                book.reviews.append(review)
                break
        else:
            print(f"{title} book not found")
    elif choice == "6": #summarize reviews
        title = input('enter the book you want the review summary for: ')

        for book in library:
            if book.title == title:
                if not book.reviews:
                    print(f"{title} book has no reviews yet")
                else: 
                    print(f"Summary: {book.summarize_reviews(book.reviews)}")
            break
        else:
            print(f"{title} book not found")
    elif choice == "7":
        print(f"good bye!")
        break
    else:
        print("enter a valid option")
