#QUESTION1
input_str = input("Enter integers with spaces in b\w: ")
n = [int(x) for x in input_str.split()]
print("Integer list", n)
even = lambda x: x % 2 == 0
even_numbers = list(filter(even, n))
print("Even integers:", even_numbers)

#QUESTION 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}' by {book.author}.")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} returned '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, member, book):
        if book in self.books and member in self.members:
            member.borrow_book(book)
        else:
            print("Invalid member or book.")

    def check_availability(self, book):
        if book.is_available:
            print(f"'{book.title}' by {book.author} is available.")
        else:
            print(f"'{book.title}' by {book.author} is not available.")