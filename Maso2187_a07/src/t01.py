"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from List_linked import List

# Constants

def print_list(list1):
    string = "("
    for i in list1:
        string += str(i) + ", "
    string = string[:-2] + ")"
    print(string)


list1 = List()

for i in range(10):
    list1.append(i)

print_list(list1)

target1, target2 = list1.split()

print_list(target1)
print_list(target2)

