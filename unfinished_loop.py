"""
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!
"""

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i+=1
    return res

# Test Cases
print(create_array(1)) # [1]
print(create_array(2)) # [1,2]
print(create_array(3)) # [1,2,3]