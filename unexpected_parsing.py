"""
Function should return a dictionary/Object/Hash with "status" as a key, whose value can : "busy" or "available" 
depending on the truth value of the argument is_busy.
"""

def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status": status}

# Test
print(get_status(True)) # Expected: {"status": "busy"}
print(get_status(False)) # Expected: {"status": "available