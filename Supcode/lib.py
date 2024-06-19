
class Book:
    def __init__(self, title, author, date_of_purchase):
        self.title = title
        self.author = author
        self.date_of_purchase = date_of_purchase
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

    def __str__(self):
        return f"{self.title} by {self.author}, purchased on {self.date_of_purchase}"


class Member:
    def __init__(self, name, cf):
        self.name = name
        self.cf = cf

    def __str__(self):
        return f"Member: {self.name}, CF: {self.cf}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member}")

    def list_books(self):
        for book in self.books:
            print(book)

    def list_members(self):
        for member in self.members:
            print(member)


def main():
    # Creating instances of books
    book1 = Book("Sette brevi lezioni di fisica", "Carlo Rovelli", 2013)
    book2 = Book("Il cimitero di Praga", "Umberto Eco", 2018)

    # Creating a library instance
    library = Library()

    # Adding books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Listing all books in the library
    print("\nBooks in library:")
    library.list_books()

    # Creating and registering members
    member1 = Member("Alice", "CF123456")
    member2 = Member("Roberto", "CF784589")

    library.register_member(member1)
    library.register_member(member2)

    # Listing all members
    print("\nMembers in library:")
    library.list_members()

    # Attempt to check out and return books
    print("\nChecking out and returning books:")
    book1.check_out()
    book1.return_book()
    
    book2.check_out()
    book2.return_book()


if __name__ == "__main__":
    main()








   

   


