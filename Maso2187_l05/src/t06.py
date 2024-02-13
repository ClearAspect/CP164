"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-02-08"
-------------------------------------------------------
"""
# Imports
from functions import bag_to_set

# Constants

lists = [[],
         [99],
         [11, 22, 33, 44, 55],
         [55, 44, 33, 22, 11],
         [22, 33, 11, 55, 44],
         [99, 99, 99, 99, 99],
         [22, 33, 11, 55, 44, 22, 33, 11, 55, 44, 22, 33, 11, 55, 44],
         [4, 5, 3, 4, 5, 2, 2, 4],
    ]

for list in lists:
    print(f"Original:\n{list}")
    print(f"New:\n{bag_to_set(list)}\n")