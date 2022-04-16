"""Recursion

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
Starter code for some recursive functions we'll write that operate on
nested lists.

Pattern we can often use:

    if isinstance(obj, int):
        ...
    else:
        for sublist in obj:
            ... f(sublist) ...

"""
from typing import List, Optional, Union


# This function is traced on the first worksheet.
def flatten(obj: Union[int, list]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>.

    The integers are returned in the left-to-right order they appear
    in <obj>.

    >>> flatten(6)
    [6]
    >>> flatten([1, [-2, 3], -4])
    [1, -2, 3, -4]
    >>> flatten([[0, -1], -2, [[-3, [-5]]]])
    [0, -1, -2, -3, -5]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
        for sublist in obj:
            s.extend(flatten(sublist))
        return s

# This function is traced on the first worksheet.
def uniques(obj: Union[int, List]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>, with no duplicates.

    >>> uniques([13, [2, 13], 4])
    [13, 2, 4]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
        # Lookup the set built-in type
        for sublist in obj:
            new_items = uniques(sublist)
            # Need to check whether each item in new_items is in s
            for item in new_items:
                if item not in s:
                    s.append(item)

        return s

def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """Return whether the given item appears in <obj>.
    """
    pass

def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """Return the first (leftmost) number in <obj> at depth <d>.

    Return None if there is no item at depth d.

    Precondition: d >= 0.
    """
    pass

def add_one(obj: Union[list, int]) -> None:
    """Add one to every number stored in <obj>. Do nothing if <obj> is an int.

    If <obj> is a list, *mutate* it to change the numbers stored.
    (Don't return anything in either case.)

    >>> lst0 = 1
    >>> add_one(lst0)
    >>> lst0
    1
    >>> lst1 = []
    >>> add_one(lst1)
    >>> lst1
    []
    >>> lst2 = [1, [2, 3], [[[5]]]]
    >>> add_one(lst2)
    >>> lst2
    [2, [3, 4], [[[6]]]]
    """
    pass

def consistent_depth(obj: Union[int, list]) -> bool:
    """ Return True iff obj is nested to a consistent depth throughout
    
    >>> consistent_depth(6)
    True
    >>> consistent_depth([1, 2, 3, 4])
    True
    >>> consistent_depth([[1, 2], [[3]], 4])
    False
    """
    if isinstance(obj, int):
        return True
    if len(obj) == 0:
        return True
    else:
        depth_counter = depth_determiner(obj[0])
        for item in obj:
            temp_var = depth_determiner(item)
            if temp_var != depth_counter:
                return False
        return True    


def depth_determiner(obj: Union[int, list]) -> int:
    """Determine the depth of any given nested list
    """
    if isinstance(obj, int):
        return 1
    elif obj == []:
        return 1
    else:
        depth_counter = 0
        for item in obj:
            temp = depth_determiner(item)
            depth_counter += temp
        return depth_counter

consistent_depth([1, 2, 3, 4])

if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()

    import doctest
    doctest.testmod()
