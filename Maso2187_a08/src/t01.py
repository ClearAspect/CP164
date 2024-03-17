"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""

# Imports
from copy import deepcopy
from BST_linked import BST

# Constants


# source._root > 3 1,5 0,2,4,6

tree = BST()
tree.insert(3)
tree.insert(1)
tree.insert(5)
tree.insert(0)
tree.insert(2)
tree.insert(4)
tree.insert(6)

tree2 = deepcopy(tree)
tree3 = deepcopy(tree)
tree3.insert(7)

print(20 * "-")
print(f"Testing Equality (tree1 == tree2) expecting True: {tree == tree2}")
print(f"Testing Equality (tree1 == tree3) expecting False: {tree == tree3}")
print(20 * "-")
