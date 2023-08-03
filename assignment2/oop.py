#  Create a Python class to represent a University. The university should have
# attributes like name, location, and a list of departments. Implement encapsulation to
# protect the internal data of the University class. Create a Department class that
# inherits from the University class. The Department class should have attributes like
# department name, head of the department, and a list of courses offered. Implement
# polymorphism by defining a common method for both the University and
# Department classes to display their details.

class University:
    def __init__(self,name, location, departments):
          self.name = name
          self.location = location
          self.departments = departments
    def get_name(self):
        return self._name

    def get_location(self):
        return self._location

    def get_departments(self):
        return self._departments

    def display(self):
        print("Name of University",self.name)
        print("Location:",self.location)
        print("List of departments",self.departments)

class Department(University):
    def __init__(self, university_name, university_location, departments,department_name, head_of_the_department, courses_offered):
        super().__init__(university_name, university_location, departments)

        self.department_name = department_name
        self.head_of_the_department = head_of_the_department
        self.courses_offered = courses_offered

    def get_department_name(self):  # getter method for department_name
        return self._department_name

    def get_head_of_the_department(self):  # getter method for head_of_the_department
        return self._head_of_the_department

    def get_courses_offered(self):  # getter method for courses_offered
        return self._courses_offered

    def display(self):
         super().display()
         print("Department Name:",self.department_name)
         print("HOD:",self.head_of_the_department)
         print("List of courses:",self.courses_offered)


U1 = University("Tribhuwan", "Kathmandu",["BCT","CIVIL","BEX"])
U1.display()
D1 = Department("Tribhuwan", "Kathmandu", ["BCT", "CIVIL", "BEX"],
                "BCT", "Sudeep Shakya", ["ECT", "DSA", "TOC"])
D1.display()

#  Build a Python class to represent a simple banking system. Create a class for a
# BankAccount, and another for Customer. The BankAccount class should have a
# constructor to initialize the account details (account number, balance, account type).
# The Customer class should have a constructor to set the customer's details (name,
# age, address) and create a BankAccount object for each customer. Implement a
# destructor for both classes to display a message when objects are destroyed.

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"Account {self.account_number} is being destroyed.")

class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = None

    def create_account(self, account_number, balance, account_type):
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        print(f"Customer {self.name} is being deleted.")


if __name__ == "__main__":

    customer1 = Customer("John Doe", 30, "123 Main Street, City")


    customer1.create_account("123456789", 1000, "Savings")


    print(f"{customer1.name} has a {customer1.bank_account.account_type} account with account number {customer1.bank_account.account_number} and balance {customer1.bank_account.balance}.")


    del customer1
