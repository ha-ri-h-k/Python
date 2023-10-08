class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class BookStore:
    def __init__(self):
        self.books = []
        self.cart = []

    def add_book(self, title, author, price):
        book = Book(title, author, price)
        self.books.append(book)

    def list_books(self):
        print("Available Books:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book.title} by {book.author} - Rs:{book.price:.2f}")

    def search_books(self, keyword):
        found_books = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                found_books.append(book)
        if found_books:
            print("Search Results:")
            for idx, book in enumerate(found_books, start=1):
                print(f"{idx}. {book.title} by {book.author} -Rs{book.price:.2f}")
        else:
            print("No books found !")

    def add_to_cart(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            self.cart.append(book)
            print(f"{book.title} added to your cart.")
        else:
            print("Invalid book index.")

    def view_cart(self):
        if self.cart:
            print("Your Shopping Cart:")
            for idx, book in enumerate(self.cart, start=1):
                print(f"{idx}. {book.title} by {book.author} - Rs:{book.price:.2f}")
        else:
            print("Your cart is empty.")


def main():
    my_bookstore = BookStore()
    my_bookstore.add_book("The Catcher in the Rye", "J.D. Salinger", 2000)
    my_bookstore.add_book("To Kill a Mockingbird", "Harper Lee", 2500)
    my_bookstore.add_book("1984", "George Orwell", 500)
    my_bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", 800)
    my_bookstore.add_book("Pride and Prejudice", "Jane Austen", 1200)
    my_bookstore.add_book("Moby-Dick", "Herman Melville", 980)
    my_bookstore.add_book("The Hobbit", "J.R.R. Tolkien", 780)
    my_bookstore.add_book("The Lord of the Rings", "J.R.R. Tolkien", 899)
    my_bookstore.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1299)
    my_bookstore.add_book("The Hunger Games", "Suzanne Collins", 1199)

    try:
        while True:
            print("HK Bookstore")
            print("Menu:\n")
            print("1. Books list")
            print("2. Search")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                my_bookstore.list_books()
            elif choice == "2":
                keyword = input("Enter search keyword (title or author): ")
                my_bookstore.search_books(keyword)
            elif choice == "3":
                my_bookstore.list_books()
                book_index = int(input("Enter the index of the book you want to add to the cart: "))
                my_bookstore.add_to_cart(book_index)
            elif choice == "4":
                my_bookstore.view_cart()
            elif choice == "5":
                print("Thank you for shopping with us. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid value entered")
    except KeyboardInterrupt:
        print("__ERROR_404__")

main()
