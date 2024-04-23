"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-07-11"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.

                # your code here
                node = None
            elif node._left is None:
                # node has no left child.

                # your code here
                node = node._right
            elif node._right is None:
                # node has no right child.

                # your code here
                node = node._left
            else:
                # Node has two children

                # your code here
                if node._left._right is None:
                    repl_node = node._left
                else:
                    repl_node = self._delete_node_left(node._left)
                    repl_node._left = node._left

                repl_node._right = node._right
                node = repl_node

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """

        # your code here
        
        child = parent._right

        if child._right is None:
            repl_node = child
            parent._right = child._left
        else:
            repl_node = self._delete_node_left(child)
        

        parent._update_height()
        return repl_node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        value = self.retrieve(key)
        return value is not None

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """

        # your code here


    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are equal.
        Values in self and target are compared and if all values are equal
        and in the same location, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a bst (BST)
        Returns:
            equals - True if source contains the same values
                as target in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """

        # your code here

        equals = self._eq_aux(self._root, target._root)

        return equals

    def _eq_aux(self, source, target):
        """
        ---------------------------------------------------------
        Private helper functions for __eq__ to determine whether two BSTs are equal.
        Use: equals = self._eq_aux(source._root, target._root)
        ---------------------------------------------------------
        Parameters:
            source - a bst node (BST_Node)
            target - a bst node (BST_Node)
        Returns:
            equals - True if source contains the same values as target
                in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """

        # your code here

        equals = True

        if source is not None and target is not None:
            if source._value != target._value:
                equals = False
            else:
                equals = self._eq_aux(source._left, target._left)
                if equals:
                    equals = self._eq_aux(source._right, target._right)
        elif source is None and target is not None or source is not None and target is None:
            equals = False
        
        return equals

    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"


        # your code here
        node = self._root
        parent = None
        found = False

        while node is not None and not found:
            if key < node._value:
                parent = node
                node = node._left
            elif key > node._value:
                parent = node
                node = node._right
            else:
                found = True

        if parent is None or not found:
            value = None
        else:
            value = deepcopy(parent._value)
        return value


    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"


        # your code here


        return self._parent_r_aux(self._root, key, None)

    def _parent_r_aux(self, node, key, parent):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        Private recursive operation called only by parent_r.
        ---------------------------------------------------------
        Parameters:
            node - a bst node (BST_Node)
            key - a key value (?)
            parent - the parent node of the current node (BST_Node)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """

        # your code here

        if node is None:
            value = None
        elif key < node._value:
            value = self._parent_r_aux(node._left, key, node)
        elif key > node._value:
            value = self._parent_r_aux(node._right, key, node)
        elif parent is None:
            value = None
        else:
            value = deepcopy(parent._value)
        return value


    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here


        current = self._root

        while current._right is not None:
            current = current._right


        value = deepcopy(current._value)
        return value


    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"


        # your code here


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here

        value = self._root._value
        current = self._root
        while current is not None:
            value = current._value
            current = current._left

        return value


    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here


    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """

        # your code here


        count = self._leaf_count_aux(self._root)

        return count

    def _leaf_count_aux(self, current):
        """
        ---------------------------------------------------------
        Helper functions for leaf_count.
        ---------------------------------------------------------
        Parameters:
            current - a bst node (BST_Node)
        Returns:
            count - number of nodes with no children in current's subtree (int)
        ---------------------------------------------------------
        """

        # your code here

        if current is None:
            count = 0
        elif current._left is None and current._right is None:
            count = 1
        else:
            count = self._leaf_count_aux(current._left) + self._leaf_count_aux(current._right)

        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """

        # your code here
        count = self._two_child_count_aux(self._root)

        return count

    def _two_child_count_aux(self, current):
        """
        ---------------------------------------------------------
        Helper functions for two_child_count.
        ---------------------------------------------------------
        Parameters:
            current - a bst node (BST_Node)
        Returns:
            count - number of nodes with two children in current's subtree (int)
        ---------------------------------------------------------
        """

        # your code here

        if current is None:
            count = 0
        elif current._left is not None and current._right is not None:
            count = 1 + self._two_child_count_aux(current._left) + self._two_child_count_aux(current._right)
        else:
            count = self._two_child_count_aux(current._left) + self._two_child_count_aux(current._right)

        return count


    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """

        # your code here
        

        count = self._one_child_count_aux(self._root)

        return count

    def _one_child_count_aux(self, current):
        """
        ---------------------------------------------------------
        Helper functions for one_child_count.
        ---------------------------------------------------------
        Parameters:
            current - a bst node (BST_Node)
        Returns:
            count - number of nodes with one child in current's subtree (int)
        ---------------------------------------------------------
        """

        # your code here

        if current is None:
            count = 0
        elif current._left is not None and current._right is None or current._left is None and current._right is not None:
            count = 1 + self._one_child_count_aux(current._left) + self._one_child_count_aux(current._right)
        else:
            count = self._one_child_count_aux(current._left) + self._one_child_count_aux(current._right)

        return count

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """

        # your code here

        zero = 0
        one = 0
        two = 0

        zero, one, two = self._node_counts_aux(self._root, zero, one, two)

        return zero, one, two

    def _node_counts_aux(self, current, zero, one, two):
        """
        ---------------------------------------------------------
        Helper functions for node_counts.
        ---------------------------------------------------------
        Parameters:
            current - a bst node (BST_Node)
        Returns:
            zero - number of nodes with zero children in current's subtree (int)
            one - number of nodes with one child in current's subtree (int)
            two - number of nodes with two children in current's subtree (int)
        ---------------------------------------------------------
        """

        # your code here

        

        if current is not None:
            if current._left is None and current._right is None:
                zero += 1
            elif current._left is None:
                one += 1
                zero, one, two = self._node_counts_aux(current._right, zero, one, two)
            elif current._right is None:
                one += 1
                zero, one, two = self._node_counts_aux(current._left, zero, one, two)
            else:
                two += 1
                zero, one, two = self._node_counts_aux(current._left, zero, one, two)
                zero, one, two = self._node_counts_aux(current._right, zero, one, two)

        return zero, one, two


    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """

        # your code here

        balanced = self._is_balanced_aux(self._root)

        return balanced

    def _is_balanced_aux(self, node):
        """
        ---------------------------------------------------------
        Private Helper functions to determine whether a bst is balanced.
        Use: b = self._is_balanced_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a _BST_Node (node)
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """

        # your code here

        balanced = True
        if node is not None:
            balanced = abs(self._node_height(node._left) - self._node_height(node._right)) <= 1
            if balanced:
                balanced = self._is_balanced_aux(node._left)
                if balanced:
                    balanced = self._is_balanced_aux(node._right)

        return balanced


    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper functions to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """

        # your code here


    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """

        # your code here

        valid = self._is_valid_aux(self._root)

        return valid

    def _is_valid_aux(self, node):
        """
        ---------------------------------------------------------
        Helper functions to determine if a tree is a valid BST.
        Use: b = self._is_valid_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a _BST_Node (node)
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """

        # your code here

        valid = True
        if node is not None:
            if node._left is not None:
                valid = node._left._value < node._value
            if valid and node._right is not None:
                valid = node._right._value > node._value
            if valid:
                valid = self._is_valid_aux(node._left)
                if valid:
                    valid = self._is_valid_aux(node._right)

        return valid

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """

        # your code here

        a = self._inorder_aux(self._root)
        return a

    def _inorder_aux(self, node):
        """
        ---------------------------------------------------------
        Helper functions to generate a list of the contents of the tree
        in inorder order.
        Use: a = self._inorder_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a _BST_Node (node)
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        ---------------------------------------------------------
        """

        # your code here

        a = []
        if node is not None:
            a = self._inorder_aux(node._left)
            a.append(node._value)
            a.extend(self._inorder_aux(node._right))

        return a

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """

        # your code here

        a = self._preorder_aux(self._root)

        return a

    def _preorder_aux(self, node):
        """
        ---------------------------------------------------------
        Helper functions to generate a list of the contents of the tree
        in preorder order.
        Use: a = self._preorder_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a _BST_Node (node)
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        ---------------------------------------------------------
        """

        # your code here

        a = []
        if node is not None:
            a.append(node._value)
            a.extend(self._preorder_aux(node._left))
            a.extend(self._preorder_aux(node._right))

        return a


    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """

        # your code here

        a = self._postorder_aux(self._root)

        return a

    def _postorder_aux(self, node):
        """
        ---------------------------------------------------------
        Helper functions to generate a list of the contents of the tree
        in postorder order.
        Use: a = self._postorder_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a _BST_Node (node)
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        ---------------------------------------------------------
        """

        # your code here

        a = []
        if node is not None:
            a = self._postorder_aux(node._left)
            a.extend(self._postorder_aux(node._right))
            a.append(node._value)

        return a

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """

        # your code here

        values = []

        if self._root is not None:
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                node = queue.pop(0)
                values.append(node._value)
                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)

        return values


    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """

        # your code here


    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
                    
