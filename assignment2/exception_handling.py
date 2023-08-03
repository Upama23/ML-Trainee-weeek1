#  Write a Python program that takes two integers as input and performs division
# (num1 / num2). Handle the ZeroDivisionError and display a custom error message
# when the second number is zero.

def division(num1, num2):
    try:
        result = num1/num2
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed")

result = division(4,0)
print("Division is", result)

#  Implement a program that takes user input for a filename, opens the file in read
# mode, and displays its contents. Handle the FileNotFoundError and display an error
# message if the file is not found.

def file_open(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print("File provided not fount")

content = file_open('upama')
print("Contents:",content)

#  Write a Python program that takes a user input and converts it to an integer. Handle
# the ValueError and display a custom error message when the input cannot be
# converted to an integer.

def convert_to_integer(user_input):
    try:
        integer_value = int(user_input)
        return integer_value
    except ValueError:
        print("Please enter a valid integer.")

integer_value = convert_to_integer("up")
print(f"Converted integer: {integer_value}")

#  Write a Python program that takes two integers as input and performs division (num1
# / num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
# display appropriate error messages.

def perform_division(num1, num2):
    try:
        result = int(num1) / int(num2)
        return result
    except ValueError:
        print("Please enter valid integers for both numbers.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

result = perform_division(6, "abc")
print("Result is:",result)

# Write a Python program that takes user input for age. Create a custom exception
# InvalidAgeError to handle cases where the age is below 0 or above 120.
# ○ Hint: Create new class InvalidAgeError that inherits Exception class

class InvalidAgeError(Exception):
    pass

def get_valid_age():
    try:
        age = 7
        if age < 0 or age > 120:
            raise InvalidAgeError("Invalid Age, Please provide the age betweeen 0 and 120")
        return age
    except ValueError:
        raise InvalidAgeError("Please enter valid integer")

try:
    age = get_valid_age()
    print(f"Valid age: {age}")
except InvalidAgeError as e:
    print(f"Error: {e}")

#  Implement a program that reads user input for a password. Create a custom
# exception WeakPasswordError to handle cases where the password is shorter
# than 8 characters.
# ○ Hint: WeakPasswordError that inherits Exception class

class WeakPasswordError(Exception):
    pass

def get_password():
    password = "upama"
    if len(password) < 8:
        raise WeakPasswordError("Password should be at least 8 characters.")
    return password

try:
    password = get_password()
    print("Password successfull")
except WeakPasswordError as e:
    print(f"Error: {e}")

