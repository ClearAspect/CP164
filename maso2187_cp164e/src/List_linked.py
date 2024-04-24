"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Roan Mason
ID:     169072187
Email:  maso2187@mylaurier.ca
__updated__ = "2024-04-22"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613x
# pylint: disable=E1128

# Imports
from copy import deepcopy
from pickle import FALSE


class List:
    """
    A linked List class.
    """

    def split_count(self, count):
        """
        -------------------------------------------------------
        Splits source into separate target lists based on count.
        At finish target1 contains count nodes, target2 contains 
        remaining nodes from source, and source is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_count(count)
        -------------------------------------------------------
        Parameters:
            count - the number of nodes in target1 (int >= 0)
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            target1 - contains count nodes from source (List)
            target2 - contains remaining nodes from source (List)
        -------------------------------------------------------
        """

        # Your code here
        target1 = List()
        target2 = List()
        
        if count > self._count:
            count = self._count
        
        
        for i in range(count):
            target1.append(self._remove_front())
        
        while self._count > 0:
            target2.append(self._remove_front())
            
            
        
        #for loop up to count
            #remove first node and append to the target list
        
        #while to remove remaining elements and add to target 2
        

        return target1, target2
    
    def _remove_front(self):
        
        value = self._front._value
        
        if self._count == 1:
            self._front = None
            self._rear = None
        
        else: 
            self._front = self._front._next
        
        self._count -= 1
        
        return value

    def replace_many(self, key, value):
        """
        -------------------------------------------------------
        Replace every occurrence of key in source with value.
        List is otherwise unchanged.
        Use: source.replace_many(key, value)
        -------------------------------------------------------
        Parameters:
            key - a key that may be in source (?)
            value - the replacement for key (?)
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            None.
        -------------------------------------------------------
        """

        # Your code here
        
        current = self._front
        
        for i in range(self._count):
            if current._value == key:
                current._value = value
            
            current = current._next

        return

    def rotate_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.rotate_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            None
        -------------------------------------------------------
        """

        # Your code here
        
        if self._front is not None and self._count > 1:
            original_rear = self._rear
            original_front = self._front
                        
            previous = None
            current = self._front
            while current._next is not None:
                previous = current
                current = current._next
                
            previous._next = None
            
            original_rear._next = self._front
            self._front = original_rear
            
        

        return

    def has_loop(self):
        """
        -------------------------------------------------------
        Determines if source contains a circular reference/loop.
        Use: loop = source.has_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            loop - True if source contains a circular reference,
                False otherwise (bool)
        -------------------------------------------------------
        """

        # Your code here
        
        loop = False
        
        if self._count > 1:
            
            current = self._front
            for i in range(self._count):
                current = current._next
                
            if current is not None:
                loop = True
            

        return loop

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None and count < self._count:
            yield current._value
            current = current._next
            count += 1


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌‌‌​‌​‌‌​​​‌‌‌​‌‌:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
