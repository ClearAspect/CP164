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
from Queue_circular import Queue

# Constants

queue = Queue()


print("Test insert")
for i in range(5):
    queue.insert(i)
    print(i)

print(f"Len: {len(queue)}")

if queue.is_empty():
    print("Empty")
else:
    print("not Empty")
    
if queue.is_full():
    print("Full")
else:
    print("not Full")
    
print(f"Peek: {queue.peek()}")
print(f"Remove: {queue.remove()}")

print(f"Len: {len(queue)}")

queue2 = Queue()

for i in range(5):
    queue2.insert(i)
    
if queue == queue2:
    print("Equal")
else:
    print("not Equal")
    

print()    

queue2.remove()

if queue == queue2:
    print("Equal")
else:
    print("not Equal")
    
    
print("Iterator")
for value in queue:
    print(value)