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
from functions import stack_combine
from Stack_array import Stack

# Constants


stack1 = Stack()
stack1.push(8)
stack1.push(12)
stack1.push(8)
stack1.push(5)

for i in stack1:
    print(f"{i}, ", end="")
print()

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

target = stack_combine(stack1, stack2)

for i in target:
    print(f"{i}, ", end="")
print()