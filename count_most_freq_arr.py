"""
Complete the function to find the count of the most frequent item of an array. 
You can assume that input is an array of integers. For an empty array return 0

input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5

"""

def most_frequent_item_count(collection):
    if collection:
        # Find most frequent element
        res = max(set(collection), key = collection.count)
        # Count the occurences of most frequent element
        return collection.count(res)
    return 0

# Test Cases
print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])) # 5
print(most_frequent_item_count([])) # 0