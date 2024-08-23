"""
Given a string s, write a method (function) that will return true 
if its a valid single integer or floating number or false if its not.

Valid examples, should return true:

isDigit("3")
isDigit("  3  ")
isDigit("-3.23")
should return false:

isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero")

"""


def is_digit(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

# Test the function
print(is_digit("3")) # True
print(is_digit("3.5")) # True
print(is_digit("3.5.5")) # False
print(is_digit("three")) # False
print(is_digit("3,5")) # False
print(is_digit("3,5,5")) # False