"""
Question (6 marks)

We are adding another method to the LinkedList class.  It's almost written
but 4 lines are missing. Complete those lines so that the method is correct
according to its docstring.

Rules:
- For each TODO below, write a single expression or line of code as indicated,
  without changing its indentation.
- You must not change any other code in any way. E.g., you must not modify,
  delete or add to what is there.

TO HAND IN: Add your code to this file and hand it in on MarkUs.  Be sure to
run the self-test on MarkUs to avoid failing all our tests due to a silly error.

--------------------------------------------------------------------------------
This file is Copyright (c) 2022 University of Toronto
All forms of distribution, whether as given or with any changes, are
expressly prohibited.
--------------------------------------------------------------------------------
"""
from __future__ import annotations
from typing import Any, Optional


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def biggest_except(self) -> Optional[int]:
        """
        Return the largest value in this linked list, excluding the value in the
        last node.

        If there are only 0 or 1 nodes in this linked list, return None.

        Precondition: All items in this linked list are ints.

        >>> linky = LinkedList([7, 5, 22, 18, 90])
        >>> linky.biggest_except()
        22
        >>> print(linky)
        [7 -> 5 -> 22 -> 18 -> 90]
        >>> linky = LinkedList([5])
        >>> linky.biggest_except() is None
        True
        >>> linky = LinkedList([])
        >>> linky.biggest_except() is None
        True
        >>> linky = LinkedList([12, 14, 156, 23, 5])
        >>> linky.biggest_except()
        156
        >>> linky = LinkedList([1, 3])
        >>> linky.biggest_except()
        1
        >>> linky = LinkedList([3])
        >>> linky.biggest_except() # returns nothing because first value
        >>> linky = LinkedList([2, 4, 6, 8, 10, 12])
        >>> linky.biggest_except()
        10
        """
        if self._first is None or self._first.next is None:
            return None
        else:
            curr = self._first
            biggest = curr.item
            while curr.next is not None:
                if biggest is None:
                    biggest = curr.item
                else:
                    biggest = max(biggest, curr.item)
                curr = curr.next
            return biggest


if __name__ == '__main__':
    import doctest
    doctest.testmod()
