"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-02-14"
-------------------------------------------------------
"""
# Imports
from List_linked import List

# Constants
list = List()

v = [22, 33, 11, 55, 44]
for value in v:
    list.insert(2, value)

for i in list:
    print(i)