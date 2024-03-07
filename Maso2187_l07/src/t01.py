"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-02-29"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from copy import deepcopy

# Constants


def print_list(list):
    numbers = ""
    for e in list:
        numbers += f"{e}, "

    print(f"({numbers})")
    return


source = List()
target = List()


for i in range(10):
    source.append(i)

for i in range(5, 15):
    target.append(i)

print("-" * 20)
print_list(source)
print_list(target)
print(source.is_empty())
print("-" * 20)


previous, current, index = source._linear_search(5)
print("Linear Search test (5): ", previous, current, index)
previous, current, index = source._linear_search_r(5)
print("Linear Search recursive test (5): ", previous, current, index)

print("-" * 20)
print("Is Identical (source, source): ", source.is_identical(source))
print("Is Identical (source, target): ", source.is_identical(target))
print("-" * 20)
print("Is Identical recursive (source, source): ", source.is_identical_r(source))
print("Is Identical recursive (source, target): ", source.is_identical_r(target))
print("-" * 20)
source1 = deepcopy(source)
target1, target2 = source1.split_alt()
print("Split alt: ")
print_list(target1)
print_list(target2)
target3, target4 = source1.split_alt_r()
print("Split alt recursive: ")
print_list(target1)
print_list(target2)
print("-" * 20)
target1 = List()
target2 = List()
target1.intersection(source, target)
target2.intersection_r(source, target)
print("Intersect: ")
print_list(target1)
print("Intersect recursive: ")
print_list(target2)
print("-" * 20)
target1 = List()
target2 = List()
target1.union(source, target)
target2.union_r(source, target)
print("Union: ")
print_list(target1)
print("Union recursive: ")
print_list(target2)
print("-" * 20)
target1 = deepcopy(source)
target2 = deepcopy(source)
target1.reverse()
target2.reverse_r()
print("Reverse: ")
print_list(target1)
print("Reverse recursive: ")
print_list(target2)
print("-" * 20)
