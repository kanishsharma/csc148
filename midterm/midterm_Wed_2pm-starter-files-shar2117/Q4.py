"""
Question (5 marks)

Implement the function below according to the docstring provided.

Rules:
- You may use the Stack and Queue classes provided in module 'adts' to
  create temporary Stack and/or Queue objects. These are the same Stack and
  Queue classes you have seen before.
- You must NOT create any other compound objects (lists, dictionaries, etc.)
- You may create variables to store individual values (counters, items that
  have been popped or dequeued, etc.)
- You may add doctest examples if desired.

Hint: You may find it helpful to use modular division by 2, that is, "% 2".

TO HAND IN: Add your code to this file and hand it in on MarkUs.  Be sure to
run the self-test on MarkUs to avoid failing all our tests due to a silly error.

--------------------------------------------------------------------------------
This file is Copyright (c) 2022 University of Toronto
All forms of distribution, whether as given or with any changes, are
expressly prohibited.
--------------------------------------------------------------------------------
"""
from adts import Stack, Queue


def remove_every_other(q: Queue) -> None:
    """Modify q to remove every other element, starting from the element that is
    one spot behind the front of the Queue.

    Do NOT return a new Queue. Modify the one that is given.

    Precondition: There are at least two items in q.

    >>> s = Queue()
    >>> s.enqueue('one')
    >>> s.enqueue('two')
    >>> s.enqueue('three')
    >>> s.enqueue('four')
    >>> s.enqueue('five')

    >>> remove_every_other(s)
    >>> s.dequeue()
    'one'
    >>> s.dequeue()
    'three'
    >>> s.dequeue()
    'five'
    >>> s.is_empty()
    True

    >>> s = Queue()
    >>> s.enqueue(2)
    >>> s.enqueue(4)
    >>> remove_every_other(s)
    >>> s.dequeue()
    2

    >>> s = Queue()
    >>> s.enqueue(1)
    >>> s.enqueue(3)
    >>> s.enqueue(5)
    >>> s.enqueue(7)
    >>> s.enqueue(9)
    >>> remove_every_other(s)
    >>> s.dequeue()
    1
    >>> s.dequeue()
    5
    >>> s.dequeue()
    9
    """
    q2 = Queue()
    counter = 0

    while not q.is_empty():
        temp = q.dequeue()
        q2.enqueue(temp)
        counter += 1

    if counter == 2:
        temp = q2.dequeue()
        q.enqueue(temp)

    while not q2.is_empty():
        counter -= 1
        temp1 = q2.dequeue()
        if counter % 2 == 0:
            q.enqueue(temp1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
