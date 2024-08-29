"""
A comfortable word is a word which you can type always alternating the hand you type with 
(assuming you type using a QWERTY keyboard and use fingers as shown in the image below).

That being said, complete the function which receives a word and returns true if it's a comfortable word and false otherwise.

The word will always be a string consisting of only ascii letters from a to z.
"""

def comfortable_word(word):
    left = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
    right = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"]
    
    # left -> check = 1
    # right -> check =2
    
    check = 0

    for i in word:
        if i in right:
            if check != 2:
                check = 2
            else:
                return False
        else:
            if check != 1:
                check = 1
            else:
                return False
    return True

# Test Cases
print(comfortable_word("yams")) # True
print(comfortable_word("test")) # False