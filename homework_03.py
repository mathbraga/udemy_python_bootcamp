# Write a function that computes the volume of a sphere given its radius.
from math import pi
def vol(rad):
    return (4/3)*pi*(rad**3)
print(vol(2))

# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low, high+1):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is NOT in range")
ran_check(5,2,7)

# Version only returning True or False
def ran_bool(num,low,high):
    return num in range(low, high+1)
print(ran_bool(5,2,7))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    ups = 0
    lows = 0
    for char in s:
        if char.isupper():
            ups += 1
        elif char.islower():
            lows += 1
    print(f"No. of Upper case characters: {ups}")
    print(f"No. of Lower case characters: {lows}")
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):  
    mul = 1
    for n in numbers:
        mul *= n
    return mul
print(multiply([1, 2, 3, -4]))

# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    s = s.replace(" ", "")
    s_reverse = s[::-1]
    return s == s_reverse
print(palindrome("helleh"))

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(" ", "").lower()
    str1 = set(str1)
    set_alphabet = set(alphabet)
    return str1 == set_alphabet
print(ispangram("The quick brown fox jumps over the lazy dog"))