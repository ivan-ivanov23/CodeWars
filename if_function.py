"""
Create a function called _if which takes 3 arguments: 
a value bool and 2 functions (which do not take any parameters): func1 and func2

When bool is truthy, func1 should be called, otherwise call the func2.
"""

def _if(bool, func1, func2):
    # if bool, i.e., if bool == True, call func1()
    # else, call func2()
    func1() if bool else func2()

def func1():
    print("True")

def func2():
    print("False")

# Test
_if(True, func1, func2) # Expected: True
_if(False, func1, func2) # Expected: False

