"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""

# Imports
from random import randint
from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ("Bubble Sort", Sorts.bubble_sort),
    ("Insertion Sort", Sorts.insertion_sort),
    ("Merge Sort", Sorts.merge_sort),
    ("Quick Sort", Sorts.quick_sort),
    ("Selection Sort", Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here

    values = List()

    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here

    lists = List()
    for i in range(SIZE):
        list = List()
        for j in range(TESTS):
            list.append(Number(randint(0, XRANGE)))

        lists.append(list)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    
    Number.comparisons = 0
    Sorts.swaps = 0

    sorted_list = create_sorted()
    reversed_list = create_reversed()
    random_list = create_randoms()

    func(sorted_list)
    comparions_sorted = round(Number.comparisons, 0)
    swaps_sorted = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0

    func(reversed_list)
    comparions_reversed = round(Number.comparisons, 0)
    swaps_reversed = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0

    for i in random_list:
        func(i)
    comparions_random = round(Number.comparisons // TESTS, 0)
    swaps_random = round(Sorts.swaps // TESTS, 0)
    Number.comparisons = 0
    Sorts.swaps = 0

    print(
        f"{title:14} {comparions_sorted:8} {comparions_reversed:8} {comparions_random:8} {swaps_sorted:8} {swaps_reversed:8} {swaps_random:8}"
    )

    return


print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

for i in range(5):
    test_sort(SORTS[i][0], SORTS[i][1])
