class Library:

    def __init__(self, no_of_books, books):
        self.no_of_books = no_of_books
        self.books = books

    def print_all_books(self):
        for book in self.books:
            print(book)

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def get_number_of_books(self):
        return self.no_of_books


if __name__ == "__main__":
    library = Library(0, [])
    library.add_book("The Hitchhiker's Guide to the Galaxy")
    library.add_book("The Lord of the Rings")
    library.print_all_books()
    print(library.get_number_of_books())
