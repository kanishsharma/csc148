"""CSC148 Prep 6 Synthesize

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh,
Myriam Majedi, and Jaisie Sin.

=== Module Description ===
This module contains a __main__ block that defines some client code.
Define the three classes so that the example __main__ block will
run with all assertions passing and the output as described.

The provided self-test on MarkUs is the FULL test suite for this week!
This is a more robust set of tests, and there are no hidden test cases.

Your grade will correspond to the number of test cases passed. If you
pass all of them, then you will receive full marks for this prep.
As such, any unspecified behaviour that is not in the self-test is left
as a design decision for you.

Your task for this prep is to complete a program that allows a user to create
checklists with items to be done and record when items are completed:
- A checklist has a name (str) and a list of checklist items.
- A checklist item has a description (str), a deadline (date), and
  the name of the user who completed the item.
- A user has a name (str) and the total number items they have completed (int).

You will need to write one class for each of these entities.
See the __main__ block for an example of how we want to use these classes.

You may choose any reasonable way to store the necessary data. Attributes that
are of type int, str, or bool, and date may be public, but all other attributes
must be private. You may add imports from the typing module, but do NOT add any
other imports.

We will be checking for class docstrings that follow the Class Design Recipe.
You must include attribute type annotations and descriptions for all attributes.
Docstrings for your methods are NOT required.
"""
from __future__ import annotations
from datetime import date

# If you need any imports from the typing module, you may import them above.
# (e.g. from typing import Optional)


class User:
    """A class that defines the user of a checklist with their name and the
    number of tasks they have completed

    === Attributes ===
    name: the name of the user
    total_items_checked: the number of tasks completed
    """
    # Attribute types
    name: str
    total_items_checked: int

    def __init__(self, name: str) -> None:
        """Initialise an instance of the class User with their name and a
        checklist that is initially set at 0.
        """
        self.name = name
        self.total_items_checked = 0


class Checklist:
    """A class that defines a checklist that can be used to track the to-do
    items currently pending for any user with the ability to
    complete each item and remove it from the checklist

    === Attributes ===
    name: the name of the checklist
    _checklist: the list of checklist items
    """
    # Attribute types
    name: str
    _checklist: list[ChecklistItem]

    def __init__(self, name: str) -> None:
        """Initialise an instance of the Checklist class with a given name name
         and a checklist list that is initially empty
        """
        self.name = name
        self._checklist = []

    def create_item(self, name: str, curr_date: date) -> None:
        """Create a ChecklistItem in the current Checklist and add it to the
        Checklist
        """
        self._checklist.append(ChecklistItem(name, curr_date))

    def mark_item_complete(self, name: str, completer: User) -> None:
        """Mark an item with the name name in the checklist as completed by the
        completer
        """
        for item in self._checklist:
            if item.desc == name:
                item.completed = True
                item.completer = completer.name
                completer.total_items_checked += 1

    def has_item(self, item_desc: str) -> bool:
        """Determine whether the given checklist has the item as specified in i
        tem_descr
        """
        for item in self._checklist:
            if item.desc == item_desc:
                return True
        return False

    def __str__(self) -> str:
        """Print out a string that shows every item in the checklist with the
         date
        and whether it is completed or not
        """
        printed_list = []
        return_string = ''
        return_string += str(self.name) + '\n'
        for item in self._checklist:
            if item.completed is True:
                printed_list.append('[x] ' + str(item.desc) + ' ('
                                    + str(item.deadline) + '), completed by '
                                    + str(item.completer) + '\n')
            else:
                printed_list.append('[-] ' + str(item.desc) + ' ('
                                    + str(item.deadline) + ')' + '\n')
        for item in printed_list:
            return_string = return_string + item
        return return_string


class ChecklistItem:
    """A class that defines an item that goes into the checlist with a
    description, a deadline due, and the name of the user who completed
    the item on any given checklist

    === Attributes ===
    desc: the description of the checklist item
    deadline: the deadline that the item is due by
    completer: the person that completed the item
    """

    # Attribute Types
    desc: str
    deadline: date
    completer: str
    completed: bool

    def __init__(self, desc: str, deadline: date) -> None:
        """Initialise an instance of the ChecklistItem class with a
        given description and deadline
        """
        self.desc = desc
        self.deadline = deadline
        self.completer = None
        self.completed = False


if __name__ == "__main__":
    # Instantiate three users
    manila = User('Manila')
    sofija = User('Sofija')
    felix = User('Felix')

    # Instantiate a checklist
    manilas_checklist = Checklist('Planner for M')

    # Manila adds some items to the checklist, the first one she adds is Math
    # Homework due on March 1st.
    manilas_checklist.create_item('Math Homework', date(2021, 3, 1))
    manilas_checklist.create_item('pick up milk', date(2021, 2, 25))
    manilas_checklist.create_item('CSC148 A1', date(2021, 3, 2))

    # Manila finishes her CSC148 assignment and marks it complete
    manilas_checklist.mark_item_complete('CSC148 A1', manila)

    # Sofija attempts to check off an item as complete that isn't in
    # manilas_checklist.  This does nothing.
    manilas_checklist.mark_item_complete('MAT157 Review', sofija)

    # Sofija picks up milk for Manila.
    manilas_checklist.mark_item_complete('pick up milk', sofija)

    print(manilas_checklist)
    # The output is below. Notice that the order is based on the order they
    # were added to manilas_checklist.  Output:
    # Planner for M
    # [-] Math Homework (2021-03-01)
    # [x] pick up milk (2021-02-25), completed by Sofija
    # [x] CSC148 A1 (2021-03-02), completed by Manila

    # confirm the check list items are all present in the checklist
    for item_description in ['Math Homework', 'pick up milk', 'CSC148 A1']:
        assert manilas_checklist.has_item(item_description)

    # Felix completed no checklist items
    assert felix.total_items_checked == 0
    # Manila and Sofija each completed one checklist item
    assert manila.total_items_checked == 1
    assert sofija.total_items_checked == 1

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['datetime'],
        'disable': ['W0212', 'E1136']
    })
