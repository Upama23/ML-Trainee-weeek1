from functools import reduce

# [map] Write a Python function square_numbers that takes a list of integers as
# input and uses the map function to return a new list containing the square of each
# element

def squared_numbers(squares):

    squared = list(map(lambda x: x ** 2 ,squares))

    return squared

print("Square of each number using map:", squared_numbers([1,2,3,4,5]))

# [map] Create a function convert_to_uppercase that takes a list of strings as input
# and uses the map function to return a new list with all the strings converted to
# uppercase.

def convert_to_uppercase(lower_cases):

    upper_cases = list(map(lambda x: x.upper(), lower_cases))

    return upper_cases

print("Lower case to upper case:",convert_to_uppercase(['upama','SHree','MaHato']))

# [filter] Implement a function called filter_prime_numbers that takes a list of
# integers as input and uses the filter function to return a new list containing only the
# prime numbers.

def is_prime(n):

    if n <= 1 :
        return False

    for i in range(2,n):
        if n % i == 0:
            return False

    return True

def filter_prime_numbers(numbers):

    prime_numbers = list(filter(lambda x: is_prime(x),numbers))

    return prime_numbers

print("Filtered prime numbers are:",filter_prime_numbers([1,2,3,4,5,6,7,8,11]))

#  [filter] Write a Python function filter_long_strings that takes a list of strings as
# input and uses the filter function to return a new list containing strings with more
# than 5 characters.

def filter_long_strings(strings):

    long_strings = list(filter(lambda x: len(x) > 5,strings ))

    return long_strings

print("Strings with greater than 5 characters are:",filter_long_strings(["upama","shree","mahato","computer"]))

#  [reduce] Write a Python function calculate_factorial that takes an integer as input
# and uses the reduce function to return the factorial of that number.

def calculate_factorial(integer):

    factorial = reduce(lambda x, y: x * y ,range(1,integer+1))

    return factorial

print("The factorial of the number is:",calculate_factorial(5))

# [reduce] Implement a function called concatenate_strings that takes a list of
# strings as input and uses the reduce function to return a single string containing the
# concatenation of all the elements.

def concatenate_strings(strings):

    concatenate = reduce(lambda x,y:x + y ,strings)

    return concatenate

print("Concatenate string is:",concatenate_strings(["I","am","Upama","Mahato"]))