"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from Food import Food
from List_array import List

# Constants

test_list = List()

test_list.append(0)
test_list.append(1)
test_list.append(2)


print("Original List:")
for value in test_list:
    print(value)
        

key = 2
index = test_list._linear_search(key)
print("\nLinear Search Result:")
print(f"Index: {index}")


removed_food = test_list.remove(key)
print("\nAfter Removing:")
for value in test_list:
    print(value)
        

test_list.insert(1, 4)
print("\nAfter Inserting:")
for food in test_list:
    print(food)