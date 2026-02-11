# A CLI-based Library Management System using OOP, with an automated review summarization feature via API integration

import asyncio
import aiohttp
import json

class Book():
    def __init__(self, book_name, author):
        self.title = book_name
        self.author = author 
        self.isIssued = False
        self.reviews = [] 
    
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

    def to_dict(self):
        return {
            "title" = self.title,
            "author" = self.author,
            "isIssued" = self.isIssued,
            "reviews" = self.reviews
        }

    @classmethod 
    def from_dict(data):
        book = Book(data["title"], data["author"])
        book.isIssued = data["isIssued"]
        book.reviews = data["reviews"]
        return book

    async def summarize_reviews(self):
        url = "https://api.example.com/summarize"

        payload = {
            "text": " ".join(self.reviews)
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json = payload) as response:
                if response.status == 200:
                    data = await response.json()
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

def save_library():
    with open("library.json", "w") as f:
        json.dump([book.to_dict() for book in library], f)

def load_library():
    global library
    try:
        with open("library.json", "r") as f:
            data = json.load(f)
            library = [Book.from_dict(book) for book in data]
    except FileNotFoundError:
            library = []

# load library at program start
load_library()

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
        save_library()
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
            if book.title.lower() == title.lower():
                issuer = input("issued by: ")
                book.issue(issuer)
                save_library()
                break
        else:
            print(f"{title} book not found for issue")
    elif choice == "4":
        title = input("enter the book title you wish to return: ")

        for book in library:
            if book.title.lower() == title.lower(): 
                book.return_book()
                save_library()
                break
        else:
            print(f"{title} book not found for return")
    elif choice == "5": #add review
        title = input("enter book you want to review: ")
        
        for book in library:
            if book.title.lower() == title.lower():
                review = input("enter your review: ")
                book.reviews.append(review)
                save_library()
                break
        else:
            print(f"{title} book not found")
    elif choice == "6": #summarize reviews
        title = input('enter the book you want the review summary for: ')

        for book in library:
            if book.title.lower() == title.lower():
                if not book.reviews:
                    print(f"{title} book has no reviews yet")
                else: 
                    summary = asyncio.run(book.summarize_reviews())
                    print(f"Summary: {summary}")
                break
        else:
            print(f"{title} book not found")
    elif choice == "7":
        save_library()
        print(f"good bye!")
        break
    else:
        print("enter a valid option")
