"""
Each floating-point number should be formatted that only the first two decimal places are returned. 
You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

Don't round the numbers! Just cut them after two decimal places!
"""

def two_decimal_places(number):
    x = str(number)
    # split x at "." and print 
    # x1 is anything before "."
    # x2 is anything after "."
    x1 = x.partition(".")[0]
    # [:2] because we are only interested in the first 2 numbers after "."
    x2 = x.partition(".")[2][:2]
    x_final = x1 + "." + x2
    return float(x_final)

# Test Cases
print(two_decimal_places(4.659725356)) # 4.65
print(two_decimal_places(173735326.3783732637948948)) # 173735326.37