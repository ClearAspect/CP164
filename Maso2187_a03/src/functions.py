"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array
from pickle import NONE


# Constants
OPERATORS = "+-*/"


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """

    target = Stack()

    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.push(source1.pop())
        if not source2.is_empty():
            target.push(source2.pop())

    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    array = []
    stack_to_array(source, array)
    array_to_stack(source, array)


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """

    stack = Stack()
    palindrome = True

    for char in string:
        if char.isalpha():
            stack.push(char.lower())

    for i in range(len(string)):
        char = string[i]
        if char.isalpha():
            if stack.is_empty() or stack.pop() != char.lower():
                palindrome = False
                i = float("inf")

    return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """

    stack = Stack()

    for element in string.split():
        if element.isdigit():
            stack.push(float(element))
        elif element in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if element == "+":
                stack.push(operand1 + operand2)
            elif element == "-":
                stack.push(operand1 - operand2)
            elif element == "*":
                stack.push(operand1 * operand2)
            elif element == "/":
                stack.push(operand1 / operand2)
    return stack.pop()


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """

    stack = Stack()
    path = []
    stack.push("Start")
    visited = set()

    while not stack.is_empty():
        current_location = stack.pop()

        if current_location not in visited:
            visited.add(current_location)
            path.append(current_location)

            if current_location == "X":
                return path

            branches = maze[current_location]

            for branch in branches:
                stack.push(branch)

        else:
            unvisited_branch = None
            while path and unvisited_branch is None:
                last_location = path[-1]
                branches = maze[last_location]

                for branch in branches:
                    if branch not in visited:
                        unvisited_branch = branch

                if unvisited_branch is not None:
                    # Found an unvisited branch, break the loop
                    stack.push(unvisited_branch)
                else:
                    path.pop()

    return None
