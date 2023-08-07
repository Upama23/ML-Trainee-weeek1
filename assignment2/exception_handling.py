#  Write a Python program that takes two integers as input and performs division
# (num1 / num2). Handle the ZeroDivisionError and display a custom error message
# when the second number is zero.
"""
This module contains examples of handling exceptions in Python.
"""

def division(num1, num2):
    """
    Perform division (num1 / num2) and handle ZeroDivisionError.
    """
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed")

div_result = division(4, 0)
print("Division is", div_result)

#  Implement a program that takes user input for a filename, opens the file in read
# mode, and displays its contents. Handle the FileNotFoundError and display an error
# message if the file is not found.

def file_open(filename):
    """
    Open a file in read mode and display its contents, handling FileNotFoundError.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print("File provided not fount")

content = file_open('upama')
print("Contents:", content)

#  Write a Python program that takes a user input and converts it to an integer. Handle
# the ValueError and display a custom error message when the input cannot be
# converted to an integer.

def convert_to_integer(user_input):
    """
    Convert user input to an integer, handling ValueError.
    """
    try:
        integer_value = int(user_input)
        return integer_value
    except ValueError:
        print("Please enter a valid integer.")
        return None

integer_values = convert_to_integer("up")
if integer_values is not None:
    print(f"Converted integer: {integer_values}")

#  Write a Python program that takes two integers as input and performs division (num1
# / num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
# display appropriate error messages.

def perform_division(num1, num2):
    """
    Convert user input to an integer, handling ValueError.
    """
    try:
        result = int(num1) / int(num2)
        return result
    except ValueError:
        print("Please enter valid integers for both numbers.")
        return None
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None

div_result = perform_division(6, "abc")
if div_result is not None:
    print("Result is:", div_result)

# Write a Python program that takes user input for age. Create a custom exception
# InvalidAgeError to handle cases where the age is below 0 or above 120.
# ○ Hint: Create new class InvalidAgeError that inherits Exception class

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""

def get_valid_age():
    """
    Get a valid age between 0 and 120, handling InvalidAgeError.
    """
    try:
        age = 7
        if age < 0 or age > 120:
            raise InvalidAgeError("Invalid Age, Please provide the age betweeen 0 and 120")
        return age
    except ValueError as exc:
        raise InvalidAgeError("Please enter valid integer") from exc

AGE = get_valid_age()
if AGE is not None:
    print(f"Valid age: {AGE}")

#  Implement a program that reads user input for a password. Create a custom
# exception WeakPasswordError to handle cases where the password is shorter
# than 8 characters.
# ○ Hint: WeakPasswordError that inherits Exception class

class WeakPasswordError(Exception):
    """Custom exception for weak passwords."""

def get_password():
    """
    Get a password, handling WeakPasswordError.
    """
    password = "upama"
    if len(password) < 8:
        raise WeakPasswordError("Password should be at least 8 characters.")
    return password

try:
    PASSWORD = get_password()
    print("Password successfull")
except WeakPasswordError as e:
    print(f"Error: {e}")
