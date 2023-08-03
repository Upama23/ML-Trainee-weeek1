#  Write a Python function called check_odd_even that takes an integer as input and
# uses a ternary operator to return "Even" if the number is even, and "Odd" if the
# number is odd.

def check_odd_even(n):

    return "Even" if n % 2 ==0 else "Odd"

print("The number is:", check_odd_even(6))

#  Create a Python function check_leap_year that takes a year as input and uses a
# ternary operator to determine if it's a leap year. Return "Leap Year" if it is, otherwise
# "Not a Leap Year." (A leap year is divisible by 4, except for years divisible by 100
# but not divisible by 400).

def check_leap_year(year):

    return "Leap year" if year % 4== 0 and (year % 100 != 0 or year % 400 ==0 ) else "Not a Leap Year"

print("The given year is:",check_leap_year(2000))

# Write a function find_bigger_number that takes three integers as input and uses a
# ternary operator to return the larger number. If all numbers are equal, return
# "Equal."

def find_bigger_number(x,y,z):

    return x if x > y and x > z else (y if y>x and y>z else (z if z >x and z > y else "Equal"))

print("The number is:", find_bigger_number(6,6,6))

# Implement a function called check_prime that takes a positive integer as input and
# uses a ternary operator to determine if it's a prime number. Return "Prime" if it is,
# otherwise "Not Prime."

def check_prime(n):

    return "Prime" if all(n % i != 0 for i in range(2,n)) else "Not Prime"

print("The provided number is:", check_prime(10))