
import sys
sys.path.append(r"D:\projectDataStructure")
from customer import Customer
from .customer import Customer
from .transaction import Transaction 
from .book import Book
class Library :
    def __init__(self):
         self.customers = []
         self.books=[]
         self.transactions = []

    def add_book(self,title,author,edition,isbn):
        new_book=Book(title , author,edition,isbn)
        self.books.append(new_book)
        return f"book{title} added to the inventory "
    def update_book(self, isbn, title=None, author=None, edition=None, availability=None):
        for book in self.books:
            if book.isbn == isbn:
                book.update_details(title, author, edition, availability)
                return f"Book '{isbn}' updated."
            return "Book not found."

    def remove_book(self, isbn):
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn]
        if len(self.books) < initial_count:
            return f"Book with ISBN '{isbn}' removed from the inventory."
        return "Book not found."
    
    def search_books(self, title=None, author=None, genre=None, isbn=None):
        results = []
        for book in self.books:
            if ((title and title.lower() in book.title.lower()) or
                (author and author.lower() in book.author.lower()) or
                (genre and genre.lower() in book.genre.lower()) or
                (isbn and isbn == book.isbn)):
                results.append(book)
        return results if results else "No books found matching the criteria."
    def list_books(self):
        return [str(book) for book in self.books] if self.books else "No books in inventory."
    

  




    
    def add_customer(self, name, contact_details, membership_status="Active"):
        new_customer = Customer(name, contact_details, membership_status)
        self.customers.append(new_customer)
        return f"Customer '{name}' added to the system."

    def update_customer(self, name, contact_details=None, membership_status=None):
        for customer in self.customers:
            if customer.name == name:
                customer.update_info(contact_details=contact_details, membership_status=membership_status)
                return f"Customer '{name}' updated."
        return "Customer not found."

    def remove_customer(self, name):
        initial_count = len(self.customers)
        self.customers = [customer for customer in self.customers if customer.name != name]
        if len(self.customers) < initial_count:
            return f"Customer '{name}' removed from the system."
        return "Customer not found."

    def list_customers(self):
        return [str(customer) for customer in self.customers] if self.customers else "No customers in the system."
    


    def checkout_book(self, book_isbn, customer_name):
        book = next((b for b in self.books if b.isbn == book_isbn), None)
        customer = next((c for c in self.customers if c.name == customer_name), None)

        if book and customer:
            transaction = Transaction(book, customer)
            self.transactions.append(transaction)
            return transaction.checkout()
        return "Book or customer not found."

    def return_book(self, book_isbn, customer_name):
        transaction = next((t for t in self.transactions if t.book.isbn == book_isbn and t.customer.name == customer_name and not t.returned), None)

        if transaction:
            return transaction.return_book()
        return "Transaction not found or book already returned."

    def generate_transaction_report(self, book_isbn, customer_name):
        transaction = next((t for t in self.transactions if t.book.isbn == book_isbn and t.customer.name == customer_name), None)

        if transaction:
            return transaction.generate_report()
        return "Transaction not found."