"""
Write a function that returns the total surface area and volume of a box as an array: [area, volume]
"""

def get_size(w,h,d):
    area = 2*d*w + 2*d*h + 2*w*h
    volume = w*h*d
    return [area, volume]

# Test Cases
print(get_size(4, 2, 6)) # [88, 48]
print(get_size(1, 1, 1)) # [6, 1]
