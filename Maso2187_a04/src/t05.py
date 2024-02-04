"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

# Constants

queue1 = Priority_Queue()

queue1.insert("A")
queue1.insert("B")
queue1.insert("C")
queue1.insert("D")
queue1.insert("E")
queue1.insert("F")
queue1.insert("G")
queue1.insert("H")

for e in queue1:
    print(f"{e}, ", end="")
print()


queue2, queue3 = pq_split_key(queue1, "D")

for e in queue2:
    print(f"{e}, ", end="")
print()

for e in queue3:
    print(f"{e}, ", end="")
print()
