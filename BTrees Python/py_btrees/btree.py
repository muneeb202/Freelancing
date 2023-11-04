import bisect
from typing import Any, List, Optional, Tuple, Union, Dict, Generic, TypeVar, cast, NewType
from disk import DISK, Address
from btree_node import BTreeNode, KT, VT, get_node

"""
----------------------- Starter code for your B-Tree -----------------------

Helpful Tips (You will need these):
1. Your tree should be composed of BTreeNode objects, where each node has:
    - the disk block address of its parent node
    - the disk block addresses of its children nodes (if non-leaf)
    - the data items inside (if leaf)
    - a flag indicating whether it is a leaf

------------- THE ONLY DATA STORED IN THE `BTree` OBJECT SHOULD BE THE `M` & `L` VALUES AND THE ADDRESS OF THE ROOT NODE -------------
-------------              THIS IS BECAUSE THE POINT IS TO STORE THE ENTIRE TREE ON DISK AT ALL TIMES                    -------------

2. Create helper methods:
    - get a node's parent with DISK.read(parent_address)
    - get a node's children with DISK.read(child_address)
    - write a node back to disk with DISK.write(self)
    - check the health of your tree (makes debugging a piece of cake)
        - go through the entire tree recursively and check that children point to their parents, etc.
        - now call this method after every insertion in your testing and you will find out where things are going wrong
3. Don't fall for these common bugs:
    - Forgetting to update a node's parent address when its parent splits
        - Remember that when a node splits, some of its children no longer have the same parent
    - Forgetting that the leaf and the root are edge cases
    - FORGETTING TO WRITE BACK TO THE DISK AFTER MODIFYING / CREATING A NODE
    - Forgetting to test odd / even M values
    - Forgetting to update the KEYS of a node who just gained a child
    - Forgetting to redistribute keys or children of a node who just split
    - Nesting nodes inside of each other instead of using disk addresses to reference them
        - This may seem to work but will fail our grader's stress tests
4. USE THE DEBUGGER
5. USE ASSERT STATEMENTS AS MUCH AS POSSIBLE
    - e.g. `assert node.parent != None or node == self.root` <- if this fails, something is very wrong

--------------------------- BEST OF LUCK ---------------------------
"""

# Complete both the find and insert methods to earn full credit
class BTree:
    def __init__(self, M: int, L: int):
        """
        Initialize a new BTree.
        You do not need to edit this method, nor should you.
        """
        self.root_addr: Address = DISK.new() # Remember, this is the ADDRESS of the root node
        # DO NOT RENAME THE ROOT MEMBER -- LEAVE IT AS self.root_addr
        DISK.write(self.root_addr, BTreeNode(self.root_addr, None, None, True))
        self.M = M # M will fall in the range 2 to 99999
        self.L = L # L will fall in the range 1 to 99999

    def insert(self, key: KT, value: VT) -> None:
        """
        Insert the key-value pair into your tree.
        It will probably be useful to have an internal
        _find_node() method that searches for the node
        that should be our parent (or finds the leaf
        if the key is already present).

        Overwrite old values if the key exists in the BTree.

        Make sure to write back all changes to the disk!
        """
        node = self._find_node(key)
        
        # Step 2: Check if the key already exists in the leaf node
        idx = node.find_idx(key)
        if idx < len(node.keys) and node.keys[idx] == key:
            # Key already exists, update the associated value
            node.data[idx] = value
        else:
            # Key doesn't exist, insert it and its associated value
            node.insert_data(key, value)
        
        # Step 3: Check if the leaf node needs to split
        if len(node.keys) > self.L:
            # Split the leaf node
            self._split_leaf(node)
        
        # Write back changes to disk
        node.write_back()


    def _find_node(self, key: KT) -> BTreeNode:
        current_node = DISK.read(self.root_addr)
        while not current_node.is_leaf:
            # Find the index where the key should be inserted or follow the last child if key is greater than all keys
            idx = bisect.bisect_left(current_node.keys, key)
            current_node = DISK.read(current_node.children_addrs[idx])
        return current_node

    def _find_node1(self, key: KT) -> BTreeNode:
        current_node = DISK.read(self.root_addr)
        while not current_node.is_leaf:
            # Find the index where the key should be inserted or follow the last child if key is greater than all keys
            idx = bisect.bisect_left(current_node.keys, key)
            if key < current_node.get_child(idx).keys[0] and key > current_node.keys[-1]:
                idx -= 1
            current_node = DISK.read(current_node.children_addrs[idx])
        return current_node

    def _split_leaf(self, node: BTreeNode):
        # Create a new sibling leaf node
        sibling_node = BTreeNode(DISK.new(), node.parent_addr, None, True)

        # Calculate the midpoint index for splitting
        midpoint = (len(node.keys) + 1) // 2

        # Move half of the keys and data to the sibling
        sibling_node.keys = node.keys[midpoint:]
        sibling_node.data = node.data[midpoint:]
        sibling_node.children_addrs = node.children_addrs[midpoint:]
        for i in range(len(sibling_node.children_addrs)):
            child = sibling_node.get_child(i)
            child.parent_addr = sibling_node.my_addr
            child.index_in_parent = i
            child.write_back()

        if len(node.children_addrs) > 0 and midpoint > 1:
            node.keys = node.keys[:midpoint - 1]
        else:
            node.keys = node.keys[:midpoint]
        node.data = node.data[:midpoint]
        node.children_addrs = node.children_addrs[:midpoint]

        # Update is_leaf attribute for the original node and sibling node
        isleaf = False
        if len(node.children_addrs) == 0:
            isleaf = True

        node.is_leaf = isleaf
        sibling_node.is_leaf = isleaf

        # Update parent references
        if node.parent_addr is None:
            # The current node is the root, so create a new root
            new_root = BTreeNode(DISK.new(), None, None, False)
            new_root.keys = [node.keys[-1]]
            new_root.children_addrs = [node.my_addr, sibling_node.my_addr]
            node.parent_addr = new_root.my_addr
            sibling_node.parent_addr = new_root.my_addr
            self.root_addr = new_root.my_addr
            node.index_in_parent = 0
            sibling_node.index_in_parent = 1
            new_root.write_back()
            node.write_back()
            sibling_node.write_back()
        else:
            # Update the parent's children addresses and index_in_parent
            parent = node.get_parent()
            idx = node.index_in_parent
            parent.keys.insert(idx, node.keys[-1])
            parent.children_addrs.insert(idx + 1, sibling_node.my_addr)
            sibling_node.index_in_parent = idx + 1
            for i in range(idx + 2, len(parent.children_addrs)):
                child = parent.get_child(i)
                child.index_in_parent += 1
                child.write_back()
            node.write_back()
            sibling_node.write_back()
            if len(parent.children_addrs) > self.M:
                self._split_leaf(parent)
                parent.is_leaf = False
            parent.write_back()

        # Write back changes to disk for both nodes
        

    def find(self, key: KT) -> Optional[VT]:
        """
        Find a key and return the value associated with it.
        If it is not in the BTree, return None.

        This should be implemented with a logarithmic search
        in the node.keys array, not a linear search. Look at the
        BTreeNode.find_idx() method for an example of using
        the builtin bisect library to search for a number in 
        a sorted array in logarithmic time.
        """
        node = self._find_node1(key)  # Find the leaf node where the key should be located

        # Perform a binary search within the node's keys
        idx = bisect.bisect_left(node.keys, key)

        if idx < len(node.keys) and node.keys[idx] == key:
            # Key found, return the associated value
            return node.data[idx]
        else:
            # Key not found
            return None

    def delete(self, key: KT) -> None:
        raise NotImplementedError("Karma method delete()")


    def print_tree(self):
        self._print_tree_recursive(self.root_addr, 0)

    def _print_tree_recursive(self, node_address: Address, depth: int):
        if node_address is not None:
            node = DISK.read(node_address)
            print("  " * depth, end="")
            print("Keys:", node.keys)

            for child_address in node.children_addrs:
                self._print_tree_recursive(child_address, depth + 1)

# btree = BTree(4, 4)
# btree.insert(10, 100)
# btree.insert(40, 100)
# btree.insert(30, 100)
# btree.insert(20, 100)
# btree.insert(25, 100)
# btree.insert(5, 100)
# btree.insert(0, 100)
# btree.insert(15, 100)
# btree.insert(17, 100)
# btree.insert(18, 100)
# btree.print_tree()
# btree.insert(19, 100)
# btree.insert(21, 100)
# btree.print_tree()