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
from functions import stack_reverse 
from Stack_array import Stack

# Constants

stack2 = Stack()
stack2.push(14)
stack2.push(9)
stack2.push(7)
stack2.push(1)
stack2.push(6)
stack2.push(3)

for i in stack2:
    print(f"{i}, ", end="")
print()

stack_reverse(stack2)

for i in stack2:
    print(f"{i}, ", end="")
print()