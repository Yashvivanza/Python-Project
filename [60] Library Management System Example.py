'''
    Write a Library class with no_of_books and books as two instance variables.
    Write a program to create a library from this Library class and show how you can print all the books , add a book and get the number of books using different methods Show that your program does not persist the books after thr program is stopped!
'''

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.no_of_books} books." "\nThe books are ")
        for book in self.books:
            print(book)

l1 = Library()
l1.add_book('Harry Potter1')
l1.showInfo()

l1.add_book('Harry Potter2')
l1.showInfo()