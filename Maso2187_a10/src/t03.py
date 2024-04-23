"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts

# Constants

def print_list(list):   
    s = ""
    for i in list:
        s += f"{i}, "
    s = f"[{s}]"
    print(s) 

list = [15, 23, 45, 12, 78, 61, 7, 18, 24]

print_list(list)

Sorts.gnome_sort(list)

print_list(list)
