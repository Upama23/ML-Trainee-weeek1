#  [Single-Responsibility Principle (SRP)] Implement a simple program to interact with
# the library catalog system. Create a Python class Book to represent a single book with
# attributes: Title, Author, ISBN, Genre, Availability (whether the book is available for
# borrowing or not). Create another Python class LibraryCatalog to manage the
# collection of books with following functionalities:
# - Add books by storing each book objects (Hint: Create an empty list in constructor
# and store book objects)
# - get book details and get all books from the list of objects
# Lets say, we need a book borrowing process (what books are borrowed and what books
# are available for borrowing). Implement logics to integrate this requirement in the above
# system. Design the classes with a clear focus on adhering to the Single Responsibility
# Principle(SRP) which represents that "A module should be responsible to one, and
# only one, actor."

class Book:

    def __init__(self, title, author, ISBN:int, genre, availability:bool):

        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.availability = availability

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Genre: {self.genre}, Availability: {self.availability}"

class LibraryCatalog(Book):

    def __init__(self):
        self.book_details = []

    def add_book(self, book):

        self.book_details.append(book)

    def get_details(self):

        for book in self.book_details:
            print (book.__str__())

class Borrow(LibraryCatalog):

    def borrow_book(self, availability=True):

        for book in self.book_details:
            if book.availability == availability:
                print(book.__str__())


book1 = Book("Thousand Splendid Suns", "Khaled Hosseini", 1234, "life", True)

library1 = LibraryCatalog()
library1.add_book(book1)

print("Book Details:")
library1.get_details()

book2= Book("Kite Runner", "Khaled Hosseini", 14, "life", False)

library2 = LibraryCatalog()
library2.add_book(book2)

print("Book Details:")
library2.get_details()

borrow1 = Borrow()
borrow1.add_book(book1)
borrow1.add_book(book2)
print("Available books")
borrow1.borrow_book()

#  [Open-Closed Principle (OCP)] Download the python file from this link. Suppose we
# have a Product class that represents a generic product, and we want to calculate the
# total price of a list of products. Initially, the Product class only has a price attribute, and
# we can calculate the total price of products based on their prices.
# Now, let's say we want to add a discount feature, where some products might have a
# discount applied to their prices. To add this feature, we would need to modify the
# existing Product class and the calculate_total_price function, which violates the
# Open/Closed Principle. Redesign this program to follow the Open-Closed Principle
# (OCP) which represents “Software entities (classes, modules, functions, etc.) should be
# open for extension, but closed for modification.”

class Product:
    def __init__(self, price):
        self.price = price

class Discount:

    def __init__(self, discount_percent):
        self.discount_percent = discount_percent

    def get_discount(self,products):

        if products.price > 50:
            return products.price * self.discount_percent
        return 0

class calculate_total_price:

    def __init__(self, discount_strategy):

        self.discount_strategy = discount_strategy

    def calculate_total_price(self, products):
        total_price = 0
        for product in products:
            total_price += product.price - self.discount_strategy.get_discount(product)
        print (total_price)


# Using the calculate_total_price function with a list of products
products = [Product(100), Product(50), Product(75)]
discount = Discount(0.2)
cal_price = calculate_total_price(discount)
cal_price.calculate_total_price(products)

#  [Liskov Substitution Principle (LSP)] Download the python file from this link. In this
# file, there is an implementation of a banking system for account handling. There is a
# savings account and a checking account class. The checking account inherits the
# savings account as both have the same functionality and the checking account allows
# overdrafts (allow processing transactions even if there is not sufficient balance).
# Redesign this program to follow the Liskov Substitution Principle (LSP) principle which
# represents that “objects should be replaceable by their subtypes without altering
# how the program works”.

class Account():

    def __init__(self, balance) -> None:
        self.balance = balance

    def withdraw(self,amount):
        pass


class SavingsAccount(Account):

    def __init__(self,balance):
        super().__init__(balance)

    def withdraw(self, amount):
        # Savings account does not allow overdrafts
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

        else:
            print("Insufficient funds!")

class CheckingAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Checking account allows overdrafts but with a limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    # Performing actions on both accounts
    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)

#  [Interface Segregation Principle (ISP)] Download the python file from this link.
# Suppose we have an interface called PaymentProcessor that defines methods for
# processing payments and refunds. Then we have a class called
# OnlinePaymentProcessor that implements the PaymentProcessor interface. However,
# some parts of our system only need to process payments and do not handle refunds.
# Redesign this program to follow the Interface Segregation Principle (ISP) principle
# which represents that “Clients should not be forced to depend upon methods that
# they do not use. Interfaces belong to clients, not to hierarchies.” (Hint: Create two
# different classes in which one class use interfaces for process payment and another
# class can process and refund payment both)

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RefundablePaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def process_refund(self, amount):
        pass

class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class OnlineRefundablePaymentProcessor(RefundablePaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

def process_order(payment_processor, amount):
    payment_processor.process_payment(amount)

def process_order_with_refund(payment_processor, amount):
    payment_processor.process_payment(amount)
    payment_processor.process_refund(amount)

if __name__ == "__main__":
    online_payment_processor = OnlinePaymentProcessor()
    process_order(online_payment_processor, 100)

    online_refundable_payment_processor = OnlineRefundablePaymentProcessor()
    process_order_with_refund(online_refundable_payment_processor, 50)

#  [Dependency Inversion Principle (DIP)] Download the python file from this link.
# Suppose we have a NotificationService class that is responsible for sending
# notifications. The NotificationService class directly depends on the EmailSender class
# to send emails.
# In this implementation, the NotificationService class directly depends on the
# EmailSender class, which violates the Dependency Inversion Principle. The high-level
# NotificationService should not depend on the low-level EmailSender, as it tightly
# couples the classes together.
# Redesign this program to follow the Dependency Inversion Principle (DIP) principle
# which represents that “Abstractions should not depend upon details. Details
# should depend upon abstractions.”

from abc import ABC, abstractmethod

# Abstract class representing the EmailSender interface
class EmailSenderInterface(ABC):
    @abstractmethod
    def send_email(self, recipient: str, subject: str, message: str) -> None:
        pass

# Concrete implementation of the EmailSenderInterface
class EmailSender(EmailSenderInterface):
    def send_email(self, recipient: str, subject: str, message: str) -> None:
        # Code to send an email
        print(f"Sending email to {recipient}: {subject} - {message}")

# NotificationService class now depends on the EmailSenderInterface
class NotificationService:
    def __init__(self, email_sender: EmailSenderInterface):
        self.email_sender = email_sender

    def send_notification(self, recipient: str, message: str) -> None:
        self.email_sender.send_email(recipient, "Notification", message)

# Using the NotificationService to send a notification

email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification("user@example.com", "Hello, this is a notification!")