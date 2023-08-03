#*args and **kwargs

# [*args] Write a Python function that takes an arbitrary number of positional
# arguments and returns the sum of all the numbers. Test your function with various
# input cases.

def sum(*args):
    total = 0
    for arg in args:
        total = total + arg

    return total

print('Sum of all the numbers is:',sum(1,2,3,4,5,6))
print('Sum of all the numbers is:',sum(10,20,30))
print('Sum of all the numbers is:',sum(-5,-7,12))
print('Sum of all the numbers is:',sum())

#  [*args] Write a Python function concat_strings that takes any number of strings as
# arguments and returns a single concatenated string.

def concat_strings(*args):
    final = ''
    for string in args:
        final = final + string
    return final

print('The concatenated string is:',concat_strings('Upama','Mahato'))
print('The concatenated string is:',concat_strings('K','A','T','H','M','A','N','D','U'))
print('The concatenated string is:',concat_strings('I','am','doing','great'))

#  [**kwargs] Write a Python function calculate_total_cost that calculates the total
# cost of items purchased from a store. The function should accept multiple keyword
# arguments, where the key is the item name, and the value is the item's price. The
# function should return the total cost of all items.

def calculate_total_cost(**kwargs):
    total_cost = 0
    for item,values in kwargs.items():
        total_cost = values + total_cost
    return total_cost

print('The total cost of items is:',calculate_total_cost(shoes=1000, pant=2000, ring=5000))
print('The total cost of items is:',calculate_total_cost(shoes=1000, pant=2000, ring=5000, laptop=200000, bag=900))

#  [**kwargs] Create a function create_student_report that takes the student's
# name as the first argument, the student's age as the second argument, and an
# arbitrary number of keyword arguments for the subjects and their respective
# scores. The function should return a dictionary with the student's information and a
# list of subjects along with their scores.

def create_student_reeport(name, age, **kwargs):

    student = {'name':name,
               'age':age,
               'subjects':kwargs}

    return student

print("The student's information is",create_student_reeport('Upama', 23, Maths=100, ECT=91, DSA=85))


