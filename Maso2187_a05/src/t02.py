"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""

# Imports
from Sorted_List_array import Sorted_List
from copy import deepcopy

# Constants

number1list = Sorted_List()
number2list = Sorted_List()

for i in range(20):
    number1list.insert(i)

print("Testing insert")
for i in number1list:
    print(f"{i} ", end="")
print()

number1list.insert(10)
number1list.insert(21)
number1list.insert(5)
number1list.insert(15)

print("Testing insert")
for i in number1list:
    print(f"{i} ", end="")
print()

print(f"Contains 10?: {10 in number1list}")
print(f"Contains 100?: {100 in number1list}")

print("List 1 == List 2?:", number1list == number2list)
number2list = deepcopy(number1list)
print("List 1 == List 2?:", number1list == number2list)


f = number1list.index(10)
print(f"Get index of 10: {f}")
print(f"Value at index 10: {number1list[f]}")

number1list.clean()
print("Testing clean")
for i in number1list:
    print(f"{i} ", end="")
print()

print(f"Index Count: {number1list.count(21)}")
print(f"Max: {number1list.max()}")
print(f"Min: {number1list.min()}")
print(f"Peek: {number1list.peek()}")
print(f"Remove 10: {number1list.remove(10)}")
print(f"Remove front: {number1list.remove_front()}")
print(f"Remove many: {number1list.remove_many(5)}")

print("Current List")
for i in number1list:
    print(f"{i} ", end="")
print()

temp = deepcopy(number1list)
target1, target2 = number1list.split()
print("Split List")
print("Target 1")
for i in target1:
    print(f"{i} ", end="")
print()
print("Target 2")
for i in target2:
    print(f"{i} ", end="")
print()

number1list = deepcopy(temp)
target1, target2 = number1list.split_alt()
print("Split_alt List")
print("Target 1")
for i in target1:
    print(f"{i} ", end="")
print()
print("Target 2")
for i in target2:
    print(f"{i} ", end="")
print()

number1list = deepcopy(temp)
target1, target2 = number1list.split_key(15)
print("Split_key List")
print("Target 1")
for i in target1:
    print(f"{i} ", end="")
print()
print("Target 2")
for i in target2:
    print(f"{i} ", end="")
print()

union1 = Sorted_List()
union2 = Sorted_List()

for i in range(10):
    union1.insert(i)
    union2.insert(i)
union1.insert(50)
union2.insert(60)

print()
print("Union List")
union3 = Sorted_List()
print("Initial Lists")
for i in union1:
    print(f"{i} ", end="")
print()
for i in union2:
    print(f"{i} ", end="")
print()

union3.union(union1, union2)
print("Union:")
for i in union3:
    print(f"{i} ", end="")
print()
