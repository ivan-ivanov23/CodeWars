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