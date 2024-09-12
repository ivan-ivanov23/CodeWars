"""
Oh no! Timmy hasn't followed instructions very carefully and forgot how to use the new String Template feature,
 Help Timmy with his string template so it works as he expects!
"""

def build_string(*args):
    return "I like {0}!".format(", ".join(args))

# Test
print(build_string("apples")) # I like apples!
print(build_string("apples", "bananas")) # I like apples, bananas!
print(build_string("apples", "bananas", "cherries")) # I like apples, bananas, cherries!