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
from Queue_array import Queue
from functions import queue_split_alt

# Constants

queue1 = Queue()

for i in range(10):
    queue1.insert(i)
    
for e in queue1:
    print(f"{e}, ", end="")
print()

queue2, queue3 = queue_split_alt(queue1)

for e in queue2:
    print(f"{e}, ", end="")
print()

for e in queue3:
    print(f"{e}, ", end="")
print()

