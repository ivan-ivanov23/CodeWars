"""
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

35231 => [1,3,2,5,3]
"""

def digitize(n):
    # Turn the int into a str and reverse it
    n = str(n)[::-1]
    # Turn the str into a list of ints
    x = [int(i) for i in n]
    return x

# Test Cases
print(digitize(35231)) # [1,3,2,5,3]
print(digitize(348597)) # [7,9,5,8,4,3]