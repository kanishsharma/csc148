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