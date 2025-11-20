class Bookstore:
    def __init__(self, books):
#        if(type(books) != dict):
#            print("Invalid data!")
#            return
        self.books = books
    def add_book(self, title):
        self.books[title] = True
    def borrow(self, title):
        if(self.books[title] != True):
            print("Book not available!")
            return
        self.books[title] = False
    def return_book(self, title):
        self.books[title] = True
    def list_available_books(self):
        for book in self.books.keys():
            if(self.books[book] == True):
                print(book)

bookStore = Bookstore({})
bookStore.add_book("Atomic habits")
bookStore.add_book("The sugar revolution")
bookStore.list_available_books()
bookStore.borrow("Atomic habits")
bookStore.list_available_books()
bookStore.return_book("Atomic habits")
bookStore.list_available_books()