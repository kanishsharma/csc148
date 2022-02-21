"""
Question [12 marks]

In this question, you will complete a program for a food ordering system that
allows customers to place orders at various restaurants.
- An order has a description of a food item (str) and a quantity (int).
- A customer has a username (str), age (int), and the total quantity (int) of
  all food items they have ordered.
- A restaurant has a name (str) and all the orders that have been placed by each
  specific customer.
You will need to write one class for each of these entities.

In the __main__ block below is an example of how we want to use these
classes. Define the three classes so that the example __main__ block will
run with all assertions passing and the output as described.  Any unspecified
behaviour is up to you -- it will not be tested.

You may choose any reasonable way to store the necessary data. Attributes that
are of type int, str, or bool may be public, but all other attributes must be
private. You may add imports from the typing module, but do NOT add any other
imports.

Your code will be marked for correctness and design, as well as for having
class docstrings that follow the Class Design Recipe. Docstrings for your
methods are NOT required.

Save your solution in a file called Q5_solution.py and submit it on MarkUs.

--------------------------------------------------------------------------------
This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh, Myriam Majedi,
and Jaisie Sin.
"""

from __future__ import annotations
from typing import Dict


class Order:
    """A=n order at a restaurant

    === Attributes ===
    desc: a description of the food item
    quantity: the quantity of the food item ordered
    """
    # Attribute Types
    desc: str
    quantity: int

    def __init__(self, name:str, quantity: int) -> None:
        self.desc = name
        self.quantity = quantity

    def __str__(self):
        return f'Order for {self.quantity} units of {self.desc}'


class Customer:
    """A customer using the food ordering system

    === Attributes ===
    username: the username of the customer
    age: the age of the customer
    total_quantity: the total quantity of all food items ordered
    """
    # Attribute Types
    username: str
    age: int
    total_quantity: int

    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age
        self.total_quantity = 0

    def create_order(self, restaurant: Restaurant, order: Order) -> None:
        self.total_quantity += order.quantity

        if self.username not in restaurant._order_dict:
            restaurant._order_dict[self.username] = [order]
        else:
            restaurant._order_dict[self.username].append(order)


class Restaurant:
    """A restaurant on the app

    === Attributes ===
    name: the name of the restaurant
    order_dict: a dictionary of all the orders with the key being the customer
    and the values being a list of all the items that they have ordered
    """
    # Attribute Types
    name: str
    _order_dict: dict[str] = list[Order]

    def __init__(self, name: str) -> None:
        self.name = name
        self._order_dict = {}

    def get_customer_orders(self, customer: str) -> list[Order]:
        if customer in self._order_dict:
            returned_list = self._order_dict[customer]
            returned_list.reverse()
            return returned_list
        else:
            return []


if __name__ == "__main__":
    # Instantiate two restaurants
    subway = Restaurant('Subway')
    tim_hortons = Restaurant('Tim Hortons')

    # Instantiate two customers
    mario = Customer('mario123', 22)
    talia = Customer('talia999', 22)

    # mario123 orders a sub, 2 cokes, and 4 cookies.
    mario.create_order(subway, Order('turkey sub', 1))
    mario.create_order(subway, Order('coke', 2))
    mario.create_order(subway, Order('cookie', 4))

    mario_orders = subway.get_customer_orders('mario123')
    for o in mario_orders:
        assert isinstance(o, Order)
        print(o)
        # Output is (notice that the most recent orders are first):
        # Order for 4 units of cookie
        # Order for 2 units of coke
        # Order for 1 units of turkey sub


    # talia999 hasn't ordered anything from Subway (or any restaurant).
    assert subway.get_customer_orders('talia999') == []
    # diane321 isn't even a known customer.
    assert subway.get_customer_orders('diane321') == []
    # mario123 hasn't ordered anything from Tim Horton's.
    assert tim_hortons.get_customer_orders('mario123') == []

    # mario123 has ordered in total 7 units of food.
    assert mario.total_quantity == 7

    # talia999 has ordered in total 0 units of food.
    assert talia.total_quantity == 0
