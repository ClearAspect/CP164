"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year

# Constants


years = [1700, 1800, 1900, 1600, 2000, 1996, 2000, 2004, 1899, 1900, 1901]

for element in years:
    print(f"{element}: {is_leap_year(element)}")
