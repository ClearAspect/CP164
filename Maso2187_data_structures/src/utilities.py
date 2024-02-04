"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

# Constants


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    for i in range(len(source)):
        stack.push(source.pop(-1))

    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not stack.is_empty():
        target.insert(0, stack.pop())
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    # Create a new stack
    s = Stack()

    print(f"Is Empty (Empty Stack): {s.is_empty()}")

    for value in source:
        s.push(value)

    print(f"Is Empty (Non-Empty Stack): {s.is_empty()}")

    print("\nPeek and Pop on Non-Empty Stack:")
    while not s.is_empty():
        print(f"Peek: {s.peek()}, Pop: {s.pop()}")
    
    return 

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        queue.insert(source.pop(0))
    
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not queue.is_empty():
        target.append(queue.remove())
    
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    print(f"Is Empty (Empty Queue): {q.is_empty()}")

    for value in a:
        q.insert(value)

    print(f"Is Empty (Non-Empty Queue): {q.is_empty()}")

    print("\nPeek, Remove, and Length on Non-Empty Queue:")
    while not q.is_empty():
        print(f"Peek: {q.peek()}, Remove: {q.remove()}, Length: {len(q)}")

    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for i in range(len(source)):
        pq.insert(source.pop(0))
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not pq.is_empty():
        target.append(pq.remove())
    return
    
def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand
    
    print(f"Is Empty (Empty Priority Queue): {pq.is_empty()}")

    for value in a:
        pq.insert(value)

    print(f"Is Empty (Non-Empty Priority Queue): {pq.is_empty()}")

    print("\nPeek and Remove on Non-Empty Priority Queue:")
    while not pq.is_empty():
        print(f"Peek: {pq.peek()}, Remove: {pq.remove()}")

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for i in range(len(source)):
        llist.append(source.pop(0))
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        target.append(llist.pop(0))
    return

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    print(f"Is the list empty? {lst.is_empty()}")

    lst.insert(0, source[0])
    lst.insert(1, source[1])
    lst.insert(2, source[2])
    print("List after insert:")
    for item in lst:
        print(item)

    # Test remove
    removed_value = lst.remove(source[1])
    print(f"Removed value: {removed_value}")
    print("List after remove:")
    for item in lst:
        print(item)

    # Test count
    count_value = lst.count(source[0])
    print(f"Count of {source[0]}: {count_value}")

    # Test append
    lst.append(source[3])
    print("List after append:")
    for item in lst:
        print(item)

    # Test index
    index_value = lst.index(source[2])
    print(f"Index of {source[2]}: {index_value}")

    # Test find
    found_value = lst.find(source[3])
    print(f"Found value: {found_value}")

    # Test max
    max_value = lst.max()
    print(f"Maximum value: {max_value}")

    # Test min
    min_value = lst.min()
    print(f"Minimum value: {min_value}")

    print("\nFull list:")
    for item in lst:
        print(item)
    
    return