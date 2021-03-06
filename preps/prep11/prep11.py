"""Prep 11 Synthesize: Recursive Sorting Algorithms

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu and Diane Horton

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 David Liu and Diane Horton

=== Module Description ===
This file includes the recursive sorting algorithms from this week's prep
readings, and two short programming exercises to extend your learning about
these algorithms in different ways.
"""
from typing import Any, List, Tuple, Optional
from __future__ import annotations


################################################################################
# Mergesort and Quicksort
################################################################################
def mergesort(lst: List) -> List:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of mergesort; it does not mutate the
    input list.

    >>> mergesort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Divide the list into two parts, and sort them recursively.
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        # Merge the two sorted halves. Need a helper here!
        return _merge(left_sorted, right_sorted)


def _merge(lst1: List, lst2: List) -> List:
    """Return a sorted list with the elements in <lst1> and <lst2>.

    Precondition: <lst1> and <lst2> are sorted.
    """
    index1 = 0
    index2 = 0
    merged = []
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] <= lst2[index2]:
            merged.append(lst1[index1])
            index1 += 1
        else:
            merged.append(lst2[index2])
            index2 += 1

    # Now either index1 == len(lst1) or index2 == len(lst2).

    # The remaining elements of the other list
    # can all be added to the end of <merged>.
    # Note that at most ONE of lst1[index1:] and lst2[index2:]
    # is non-empty, but to keep the code simple, we include both.
    return merged + lst1[index1:] + lst2[index2:]


def quicksort(lst: List) -> List:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.

    >>> quicksort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Pick pivot to be first element.
        # Could make lots of other choices here (e.g., last, random)
        pivot = lst[0]

        # Partition rest of list into two halves
        smaller, bigger = _partition(lst[1:], pivot)

        # Recurse on each partition
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)

        # Return! Notice the simple combining step
        return smaller_sorted + [pivot] + bigger_sorted


def _partition(lst: List, pivot: Any) -> Tuple[List, List]:
    """Return a partition of <lst> with the chosen pivot.

    Return two lists, where the first contains the items in <lst>
    that are <= pivot, and the second is the items in <lst> that are > pivot.
    """
    smaller = []
    bigger = []

    for item in lst:
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)

    return smaller, bigger


################################################################################
# Synthesize exercises
################################################################################
def mergesort3(lst: List) -> List:
    """Return a sorted version of <lst> using three-way mergesort.

    Three-way mergesort is similar to mergesort, except:
        - it divides the input list into *three* lists of (almost) equal length
        - the main helper merge3 takes in *three* sorted lists, and returns
          a sorted list that contains elements from all of its inputs.

    HINT: depending on your impementation, you might need another base case
    when len(lst) == 2 to avoid an infinite recursion error.

    >>> mergesort3([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    # You must NOT use mergesort, sort, or sorted.
    if len(lst) < 2:  # We've provided the base case for you.
        return lst[:]
    else:
        third = len(lst) // 3 + 1
        second_third = third * 2 + 1

        left_sorted = mergesort3(lst[:third])
        middle_sorted = mergesort3(lst[third:second_third])
        right_sorted = mergesort3(lst[second_third:])

        return merge3(left_sorted, middle_sorted, right_sorted)


def merge3(lst1: List, lst2: List, lst3: List) -> List:
    """Return a sorted list with the elements in the given input lists.

    Precondition: <lst1>, <lst2>, and <lst3> are all sorted.

    This *must* be implemented using the same approach as _merge; in particular,
    it should use indexes to keep track of where you are in each list.
    This will keep your implementation efficient, which we will be checking for.

    Since this involves some detailed work with indexes, we recommend splitting
    up your code into one or more helpers to divide up (and test!) each part
    separately.
    """
    index1 = 0
    index2 = 0
    merge = []
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] <= lst2[index2]:
            merge.append(lst1[index1])
            index1 += 1
        else:
            merge.append(lst2[index2])
            index2 += 1
    return _merge(merge + lst1[index1:] + lst2[index2:], lst3)


def kth_smallest(lst: List, k: int) -> Any:
    """Return the <k>-th smallest element in <lst>.

    Raise IndexError if k < 0 or k >= len(lst).
    Note: for convenience, k counts from 0, so kth_smallest(lst, 0) == min(lst).

    Precondition: <lst> does not contain duplicates.

    >>> kth_smallest([10, 20, -4, 3], 0)
    -4
    >>> kth_smallest([10, 20, -4, 3], 2)
    10
    """
    if len(lst) == 1 and k == 0:
        return lst[0]
    else:
        if k < 0 or k >= len(lst):
            raise IndexError
        pivot = lst[0]
        smaller, bigger = _partition(lst[1:], pivot)
        if k < len(smaller):
            return kth_smallest(smaller, k)
        elif k == len(smaller):
            return pivot
        else:
            return kth_smallest(bigger, k - len(smaller) - 1)
        
class Employee:
    """An Employee: an employee in an organization.
    === Attributes ===
    name: The name of the Employee.
    position: The name of the Employee???s position within the organization.
    superior: The superior of the Employee in the organization.
    subordinates: A list of the Employee???s direct subordinates.
    """
    name: str
    salary: float
    superior: Optional[Employee]
    subordinates: List[Employee]
    def __init__(self, name: str, salary: float) -> None:
        """Initialize this Employee."""
        self.name, self.salary = name, salary
        self.superior, self.subordinates = None, []
        class PartTimeEmployee(Employee):
            """A part-time employee in an organization.
            === Attributes ===
            fraction: float
            # plus all inherited attributes
            """
            def __init__(self, name: str, salary: float, fraction: float) -> None:
                """Initialize this PartTimeEmployee."""
                super().__init__(name, salary * fraction)
                self.fraction = fraction
    
        def make_part_time(self, fraction: float) -> None:
            """Make this Employee a PartTimeEmployee with fraction <fraction>.
            If this Employee is already a PartTimeEmployee, do nothing.
            >>> e = Employee('Anna', 100.0)
            >>> e2 = Employee('Boss', 200.0)
            >>> e3 = Employee('Minion', 50.0)
            >>> e.superior = e2
            >>> e2.subordinates.append(e)
            >>> e.subordinates.append(e3)
            >>> e3.superior = e
            >>> e.make_part_time(0.8)
            >>> len(e.superior.subordinates)
            1  
            >>> pte = e.superior.subordinates[0]
            >>> pte.name, pte.salary, pte.fraction
            ('Anna', 80.0, 0.8)  
            >>> pte.subordinates[0] is e3
            True  
            >>> pte is e
            False  
            """
            
            if isinstance(self, PartTimeEmployee):
                pass
            else:
                superior = self.superior
                subordinates = self.subordinates
                new_person = PartTimeEmployee.__init__(self, self.name, self.salary, self.fraction)
                superior.subordinates.remove(self)
                superior.subordinates.append(new_person)
                for subordinate in self.subordinates:
                    subordinate.superior = new_person
                self.superior = superior
                self.subordinates = subordinates

def freeze_list(list_) -> list:
    if isinstance(list_, int):
        return list_
    else:
        lst2 = list_[:]
        for i in range(len(lst2)):
            lst2[i] = freeze_list(lst2[i])
        return lst2

def solve(x, y):
    try: 
        if x > 50:
            raise ValueError
        a = x/y
        solution = 2 * a
        print(solution)
    except ZeroDivisionError:
        print('Cannot divide by 0')
    except NameError:
        print('Name not defined inside')
    except:
        print('Something is wrong')
    finally:
        print('End of program')
    
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all(config={'disable': ['E1136']})
