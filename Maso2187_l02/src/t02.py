"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
import utilities
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array, stack_test

# Constants

source = [11, 22, 33, 44]
stack = Stack()
print(f"Source: {source}")
print(f"Stack: {stack._values}")

array_to_stack(stack, source)

print(f"Source: {source}")
print(f"Stack: {stack._values}")

stack_to_array(stack, source)

print(f"Source: {source}")
print(f"Stack: {stack._values}")

stack_test(source)

