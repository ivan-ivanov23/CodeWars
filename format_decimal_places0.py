"""
Each number should be formatted that it is rounded to two decimal places. 
You don't need to check whether the input is a valid number because only valid numbers are used in the tests.
"""

def two_decimal_places(n):
    return float("{:.2f}".format(n))


# Test the function
print(two_decimal_places(5.5589)) # 5.56
print(two_decimal_places(3.3424)) # 3.34