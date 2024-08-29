"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

def move_zeros(lst):
    # Count num of zeros in lst
    zero_count = lst.count(0)
    # new list without zeros
    lst = [i for i in lst if i != 0]
    # Extend the list by creating a new list with the approapriate num of zeros
    # and appending it to the end of the original
    lst.extend([0] * zero_count)
    return lst

# OR
def move_zeros2(lst):
    move = 0
    for i in lst:
        if i == move:
            lst.remove(i)
            lst.append(0)
    return lst

# Test Cases
print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # [1, 1, 2, 1, 3, 0, 0]
print(move_zeros2([1, 0, 1, 2, 0, 1, 3])) # [1, 1, 2, 1, 3, 0, 0]