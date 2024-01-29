"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack

# Constants

test_strings = ["racecar", "Otto", "Able was I ere I saw Elba", "A man, a plan, a canal, Panama!", "Roan Mason"]

for test_string in test_strings:
    palindrome = is_palindrome_stack(test_string)
    print(f'"{test_string}" is a palindrome: {palindrome}')