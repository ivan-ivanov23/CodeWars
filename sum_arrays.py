"""
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0
"""

def sum_array(array):
    return sum(array) if len(array) != 0 else 0

# Test
print(sum_array([1, 5.2, 4, 0, -1])) # Expected: 9.2
print(sum_array([])) # Expected: 0
print(sum_array([1, 2, 3])) # Expected: 6