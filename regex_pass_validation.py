"""
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a digit
only contains alphanumeric characters (note that '_' is not alphanumeric)
"""

import re

regex = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)

# Test
def test_pass(password):
    return bool(re.match(regex, password))

print(test_pass("fjd3IR9")) # Expected: True
print(test_pass("ghdfj32")) # Expected: False
print(test_pass("00000")) # Expected: False