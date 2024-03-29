"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

# Constants

hash_set = Hash_Set(10)


for i in range(10):
    hash_set.insert(i)

hash_set.insert(4.56)


hash_set.debug()