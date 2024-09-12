"""
Create a function named (combine_names) that accepts two parameters (first and last name). 
The function should return the full name.

combine_names('James', 'Stevens') -> 'James Stevens'
"""

def combine_names1(f_name, l_name):
    return f_name + " " + l_name

# Test the function
print(combine_names1("John", "Star")) # 'John Star'
print(combine_names1("Ana", "Black")) # 'Ana Black'
