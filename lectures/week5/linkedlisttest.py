from typing import Any, List, Optional
from __future__ import annotations


class _Node:
    """ A node in a linked list.
    
    Considered a private class
    
    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes    
    """
    item: Any
    next: Optional[_Node]
    
    def __init__(self, item: Any) -> None:
        """ Intialise a new node storing item, with no next node.
        """
        self.item = item
        self.next = None 


class LinkedList:
    """
    A linked list implementation of the List ADT.
    """
    #=== Private Attributes ===
    # The first node in this linked list, or None if the list is empty.
    _first: Optional[_Node]
    
    def __init__(self) -> None:
        """Initialise an empty linked list
        """
        self._first = None
        
    def print_items(self) -> None:
        """Print out each item in this linked list"""
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next
    # Use the same idea of establishing the first value
    # checking if you're at the end of the list, using that 
    # condition to traverse through the list
    # and performing operations while reestablishing the index 