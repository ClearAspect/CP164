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

# Constants

queue1 = Queue()

for i in range(10):
    queue1.insert(i)
    
for e in queue1:
    print(f"{e}, ", end="")
print()

queue2, queue3 = queue1.split_alt()

for e in queue2:
    print(f"{e}, ", end="")
print()

for e in queue3:
    print(f"{e}, ", end="")
print()
