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
queue2 = Queue()
queue3 = Queue()

for i in range(5):
    queue1.insert(i)
    queue2.insert(i)
    queue3.insert(i+1)


if queue1 == queue2:
    print(f"1 and 2 Equal")
else:
    print(f"1 and 2 Not Equal")
    
if queue1 == queue3:
    print(f"1 and 3 Equal")
else:
    print(f"1 and 3 Not Equal")