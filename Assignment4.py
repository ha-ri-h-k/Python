#1. Lambda Functions#######################################33
#############################
# Question 1: Even Number Detector
#
# You are developing a program to process a list of numbers in Python. You've heard about the concept of lambda functions and want to use them for your application.
# Your task is to create a lambda function that will filter out all the even numbers from a given list of integers.
#
# Write a Python program that takes a list of integers as input and uses a lambda function to filter out the even numbers from the list.
# The program should then print the list of even numbers.

#
# Your program should follow these steps:
#
# Define a list of integers.
# Define a lambda function that takes a number as its argument and returns True if the number is even, and False otherwise.
# Use the filter() function along with the lambda function to filter out the even numbers from the list of integers.
# Convert the filtered result into a list and print it.
# Your program should output only the even numbers from the input list.
#1st Question
def main():
    input_string = input("Enter a list of integers separated by spaces: ")
    num = [int(x) for x in input_string.split()]
    print("Inputed integer list",num)
    is_even = lambda x: x % 2 == 0
    even_no= list(filter(is_even, num))
    print("Even number list:",even_no)
main()

###############################################################################################
#3rd Question

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def lend(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < 3 and book.lend():
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if member and book:
            if member.borrow_book(book):
                print(f"Book '{book_title}' lent to {member.name}.")
            else:
                print("Book not available or member reached borrowing limit.")
        else:
            print("Member or book not found.")

    def check_book_availability(self, book_title):
        book = next((b for b in self.books if b.title == book_title), None)
        if book:
            availability = "available" if book.available else "not available"
            print(f"Book '{book_title}' is {availability}.")
        else:
            print("Book not found.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Lend Book")
        print("4. Check Book Availability")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book = Book(title, author)
            library.add_book(book)
            print(book.title,book.author,"Book added successfully.")

        elif choice == 2:
            name = input("Enter member name: ")
            member_id = int(input("Enter member ID: "))
            member = Member(name, member_id)
            library.register_member(member)
            print(name,member_id,"Member registered successfully.")

        elif choice == 3:
            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title: ")
            library.lend_book(member_id, book_title)

        elif choice == 4:
            book_title = input("Enter book title: ")
            library.check_book_availability(book_title)

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please try again.")

main()
############################################################################################################################
#2nd Question


