class Book:
    def __init__ (self, title,author):
        self.title=title
        self.author=author
        self._is_checked_out=False
    def check_out_book(self):
        if not self._is_checked_out:
            self._is_checked_out=True
            return True
        return False
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out=False
            return True
        return False
    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books=[]
    def add_book(self,book):
        self._books.append(book)
    def check_out_book(self,title):
        for book in self._books:
            if (book.title.lower() == title.lower()) and book.is_available():
                book.check_out_book()
                print(f"You have checked out '{book.title}'.")
        print(f"'{title}' is not available or does not exist in the library.")
    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                print(f"'{book.title}' has been returned.")
                return
        print(f"'{title}' was not checked out or does not exist in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")