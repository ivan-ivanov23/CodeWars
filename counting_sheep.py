"""
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.
"""

def count_sheeps(sheep):
    # Using list count() method to count the True occurences
    return sheep.count(True)

# Test
print(count_sheeps([True, False, True])) # Expected: 2
print(count_sheeps([True, True, True, False])) # Expected: 3