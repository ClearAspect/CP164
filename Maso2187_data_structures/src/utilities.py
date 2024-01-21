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

    # Test is_empty on an empty stack
    print(f"Is Empty (Empty Stack): {s.is_empty()}")

    # Push elements onto the stack
    for value in source:
        s.push(value)

    # Test is_empty on a non-empty stack
    print(f"Is Empty (Non-Empty Stack): {s.is_empty()}")

    # Test peek and pop on a non-empty stack
    print("\nPeek and Pop on Non-Empty Stack:")
    while not s.is_empty():
        print(f"Peek: {s.peek()}, Pop: {s.pop()}")
