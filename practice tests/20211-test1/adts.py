"""
Question (6 marks)

Implement the function 'remove_duplicates' according to the docstring provided.

You may use the Stack and Queue classes provided in module 'adts' to
create temporary Stack and/or Queue objects. These are the same Stack and
Queue classes you have seen before.

You must NOT create any other compound objects (lists, dictionaries, sets,
etc.)

You may create variables to store individual elements (counters, items that
have been popped or dequeued, etc.)

You may add doctest examples if desired.

Save your solution in a file called Q3_solution.py and hand it in on MarkUs.

--------------------------------------------------------------------------------
This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh, Myriam Majedi,
and Jaisie Sin.
"""

from lectures.week4.adts import Stack, Queue


def remove_duplicates(q: Queue) -> None:
    """Remove duplicates from the sorted Queue q.

    The order of items in Queue q will be the same both before and after
    remove_duplicates is called.

    Two items a and b are considered duplicates if a == b.

    Preconditions:
    - The items in q can be compared using ==, !=, <, >, etc.
    - q is either sorted in non-decreasing or non-increasing order

    >>> q = Queue()
    >>> q.enqueue(2)
    >>> q.enqueue(4)
    >>> q.enqueue(4)
    >>> q.enqueue(4)
    >>> q.enqueue(5)
    >>> q.enqueue(8)
    >>> q.enqueue(8)
    >>> remove_duplicates(q)
    >>> q.dequeue()
    2
    >>> q.dequeue()
    4
    >>> q.dequeue()
    5
    >>> q.dequeue()
    8
    >>> q.is_empty()
    True
    """
    """ check_queue = Queue()
    check = q.dequeue()
    next1 = q.dequeue()

    while not q.is_empty():
        if check is None:
            q = check_queue
            return None
        elif check != next1:
            check_queue.enqueue(check)
            check_queue.enqueue(next1)
        else:
            next1 = q.dequeue()
    q = check_queue """

    q2 = Queue()
    while not q.is_empty():
        elem = q.dequeue()
        q2.enqueue(elem)
    one = None
    while not q2.is_empty():
        two = q2.dequeue()
        if one != two:
            q.enqueue(two)
        one = two








