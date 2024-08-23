"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.
"""

def sum_array(arr):
    if arr is None:
        return 0
    else:
        arr.sort()
        arr = arr[1:-1]
        res = sum(arr)
        return res
    
# Test the function
print(sum_array([6, 2, 1, 8, 10])) # 16
print(sum_array([6])) # 0