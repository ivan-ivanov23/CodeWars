"""
Complete the function so that it finds the average of the three scores passed to it 
and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
"""

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) // 3
    if 90 <= score <= 100:
        return "A" 
    if 80 <= score < 90:
        return "B"
    if 70 <= score < 80:
        return "C"
    if 60 <= score < 70:
        return "D"
    return "F"


# Test function
print(get_grade(95, 90, 93))  # Expected: 'A'
print(get_grade(70, 70, 100))  # Expected: 'B'
print(get_grade(70, 70, 70))  # Expected: 'C'