"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-02-06"
-------------------------------------------------------
"""
# Imports
from functions import vowel_count

# Constants


s1 = "BCDaFeGiHoJuXYZ"
s2 = "aeiouAEIOU"
strings = [s1, s2]

for s in strings:
    print(s)
    v = vowel_count(s)
    print(v)