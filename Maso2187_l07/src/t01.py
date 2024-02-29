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

# Constants


def print_list(list):
    numbers = ""
    for e in list:
        numbers += f"{e}, "

    print(f"({numbers})")
    return


test = List()

for i in range(10):
    test.append(i)

print("-" * 20)
print_list(test)
print(test.is_empty())
print("-" * 20)


previous, current, index = test._linear_search(5)
print("Linear Search test (5): ", previous, current, index)
previous, current, index = test._linear_search_r(5)
print("Linear Search recursive test (5): ", previous, current, index)
