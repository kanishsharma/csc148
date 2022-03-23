from typing import List, Optional, Union

def sum_nested(obj: Union[int, List]) -> int:
    """Return the sum of the numbers in <obj>
    
    Return 0 if there are no numbers
    """
    if isinstance(obj, int):
        return int
    else:
        return sum([sum_nested(elem)] for elem in obj)
    

def flatten(obj) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>."""
    if isinstance(obj, int):
        return [obj]
    else:
        # s = []
        # return sum((flatten(elem) for elem in obj), s) 
        return sum([flatten(sublist) for sublist in obj], [])

def nested_list_contains(obj, item) -> bool:
    if isinstance(obj, int):
        return obj == item
    else:
        return any([nested_list_contains(sublist, item) for sublist in obj])
    

def semi_homogenous(obj) -> bool:
    """Return whether the given nested list is semi-homogenous
    
    A single integer and empty list are semi-homogenous
    In general, a list is semi-homogenous iff:
        - all of its subnested-lists are integers, or all of them are lists
        and all of its sub-nested-lists are semi-homogenous 
    """
    
    if isinstance(obj, int):
        return True
    elif obj == []:
        return True 
    else:
        all_ints = all(isinstance(sublist, int) for sublist in obj)
        all_lists = all(isinstance(sublist, list) for sublist in obj)
        all_semi = all(semi_homogenous(sublist) for sublist in obj)
        return (all_ints or all_lists) and all_semi
        