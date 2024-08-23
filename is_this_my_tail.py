"""
Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. 
To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter 
of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.
"""

def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False
    
# Test the function
print(correct_tail('Fox', 'x')) # True
print(correct_tail('Fox', 'o')) # False