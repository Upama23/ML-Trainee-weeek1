# [list comprehension] Given a list of strings, create a new list that contains only the
# strings with more than 5 characters using list comprehension.

def five_char(strings):

    more_than_five = [i for i in strings if len(i) > 5]

    return more_than_five

print("String with more than five charracter:",five_char(["Upama","Shree","Mahato","Computer"]))

#  [list comprehension] Given two lists of integers, create a list that contains the
# product of each element of the first list with the corresponding element in the
# second list using list comprehension.

def product(list1, list2):

    multiply = [i * j for i,j in zip(list1,list2)]

    return multiply

print("Product is:",product([1,2,3],[1,2,3]))

# [list comprehension] Given three lists list1, list2, and list3, each containing
# integers, write a Python program using list comprehension to generate a new list of
# unique triplets (x, y, z) where x is from list1, y is from list2, and z is from list3, such
# that x + y + z = 0.

def unique_triplets(list1, list2, list3):

    unique = [(i, j, k) for i in list1 for j in list2 for k in list3 if i + j + k == 0]
    return unique

print("Unique triplets:", unique_triplets([1, 2, 3], [-2, 4, 5], [1, 2, 3]))

#  [dictionary comprehension] Given two lists - one containing keys and another
# containing values, create a dictionary using dictionary comprehension.

def dictionanry_comprehnsion(list1, list2):

    dictionary = {x:y for x,y in zip(list1,list2)}
    return dictionary

print("Resultant dictionary is:",dictionanry_comprehnsion(["name", "age", "gender"],["upama", 23, "female"]))

#  [dictionary comprehension] Given a dictionary with students' names as keys and
# their respective scores as values, create a new dictionary that contains only the
# students who scored more than 80 using dictionary comprehension.

def distinction_holders(student):

    record = {x:y for x,y in student.items() if y > 80}
    return record

print("Resultant student with more than 80:",distinction_holders({"upama":85, "nihal":75, "sadichhya":90}))

# [dictionary comprehension] Create a dictionary using dictionary comprehension
# to represent the ASCII values of lowercase alphabets (a-z) where the keys are the
# alphabets, and the values are their corresponding ASCII values.
# ○ Hint: use ord() function to get the ASCII value of each alphabet

def ascii_lower(lower):

    ascii_dict = {char: ord(char) for char in lower}

    return ascii_dict

print("Ascii of lower case is:",ascii_lower('abcdefghijklmnopqrstuvwxyz'))

# [set comprehension] Given a list of numbers, create a set using set
# comprehension that contains only unique even numbers.

def unique_even(numbers):

    even = {x for x in numbers if x % 2 ==0 }

    return even

print("Unique even numbers is:",unique_even([1,2,3,2,4,5,6]))

# [set comprehension] Given a list of words, write a Python program to create a set
# using set comprehension that contains all the unique characters present in the
# words.

def unique_character(words):

    unique = {char for word in words for char in word}

    return unique

print("Unique character from word are:",unique_character(["apple", "banana", "orange"]))

# [set comprehension] Given two strings, write a Python program to create a set
# using set comprehension that contains all the characters that are common in both
# strings

def common_char(str1, str2):

    common = {(x,y) for x in str1 for y in str2 if x == y}

    return common

print("Common character in both strings are:",common_char("sadichhya","upama"))