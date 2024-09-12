"""
We need a function that can transform a number (integer) into a string.

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
"""

def number_to_string(num):
    n2 = str(num)
    return n2

# Test
print(number_to_string(123)) # Expected: "123"
print(number_to_string(999)) # Expected: "999"
