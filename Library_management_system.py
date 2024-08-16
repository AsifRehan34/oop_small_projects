class Book:
    def __init__(self, title, auther, year):
        self.title = title
        self.auther = auther
        self.year = year

    def info(self):
        print("Title: ", self.title)
        print("Auther: ", self.auther)
        print("Year: ", self.year)


class Fictional(Book):
    def __init__(self, title, auther, year, genre):
        super().__init__(title, auther, year)
        self.genre = genre

    def info(self):
        print("Fictional Books: ")
        super().info()
        print("Genre: ",self.genre)


class Non_fictional(Book):
    def __init__(self, title, auther, year, topic):
        super().__init__(title, auther, year)
        self.topic = topic

    def info(self):
        print("Non Fictional Books")
        super().info()
        print("Genre: ",self.topic)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.info()
            print()

    def search_auther(self, auther):
        book_authers = []
        for book in self.books:
            if book.auther == auther:
                book_authers.append(book)
        if book_authers:
            print(f"Books by Auther {auther}:")
            for book in book_authers:
                book.info()
        else:
            print("No books found by this auther")

    def search_year(self, start_year, end_year):
        book_by_year = []
        for book in self.books:
            if start_year <= book.year <= end_year:
                book_by_year.append(book)
        if book_by_year:
            print(f"Books between year:{start_year} and {end_year}: ")
            for book in book_by_year:
                book.info()
                print()
        else:
            print("no book found")


library = Library()
fictional = Fictional("Harry Potter", "J.K. Rowling", 2012, "Fantasy")
non_fictional = Non_fictional("Sapiens", "Yuval Noah Harari", 2015, "History")

library.add_book(fictional)
library.add_book(non_fictional)

library.display_books()

library.search_author('J.K. Rowling')
library.search_year(2010, 2020)