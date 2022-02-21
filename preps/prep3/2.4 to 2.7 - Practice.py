"""Inheritance Example: Companies and Employees

=== CSC148 Fall 2018 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains an illustration of *inheritance* through an abstract
Employee class that defines a common interface for all of its subclasses.

NOTE: This is an incomplete, first version of the code, with methods but
no instance attributes. Instead, it hard-codes in specific values in methods
SalariedEmployee.get_monthly_payment and HourlyEmployee.get_monthly_payment.
"""
from datetime import date
from inspect import signature

class Employee:
    """An employee of a company.

    This is an abstract class. Only subclasses should be instantiated.
    """
    id_: int
    name: str

    def __init__(self, id_: int, name: str) -> None:
        """ Initialise this employee
        """
        self.id_ = id_
        self.name = name

    def get_monthly_payment(self) -> float:
        """Return the amount that this Employee should be paid in one month.

        Round the amount to the nearest cent.
        """
        raise NotImplementedError

    def pay(self, pay_date: date) -> None:
        """Pay this Employee on the given date and record the payment.

        (Assume this is called once per month.)
        """
        payment = self.get_monthly_payment()
        print(f'An employee was paid {payment} on {pay_date}.')


class SalariedEmployee(Employee):
    """An employee whose pay is computed based on an annual salary.

    === Attributes ===
    salary: this employees annual salary

    === Representation Invariants ===
    salary >= 0
    """
    def __init__(self, id_: int, name: str, salary: float) -> None:
        """ Initialise a Salaried Employee
        """
        Employee.__init__(self, id_, name)

        #Use the exisiting __init__ superclass function above with the input
        #variables from this init function and only define non-common aspects

        self.salary = salary

    def get_monthly_payment(self) -> float:
        """Return the amount that this Employee should be paid in one month.

        Round the amount to the nearest cent.
        """
        return round(self.salary / 12, 2)

    def pay(self, pay_date: date) -> None:
        Employee.pay(self, pay_date)
        print('Payment accepted! Have a nice day!')

class HourlyEmployee(Employee):
    """An employee whose pay is computed based on an hourly rate.

    === Attributes ===
    hourly_wage: This employee's hourly rate of pay
    hours_per_month: the hours this employee works per month

    === Representation Invariants ===
    - hourly_wage >= 0
    - hours_per_month >= 0
    """
    id_: int
    name: str
    hourly_wage: float
    hours_per_month: float

    def __init__(self, id_: int, name: str, hourly_wage: float, work_time: \
            float) -> None:
        Employee.__init__(self, id_, name)
        self.hourly_wage = hourly_wage
        self.hours_per_month = work_time

    def get_monthly_payment(self) -> float:
        """Return the amount that this Employee should be paid in one month.

        Round the amount to the nearest cent.
        """
        return round(self.hourly_wage * self.hours_per_month, 2)


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()

    employees = [
        SalariedEmployee(10, 'Sam', 500000.0),
        HourlyEmployee(11, 'Bob', 20.0, 300.0),
        SalariedEmployee(12, 'Paul', 500000.0)
    ]

    for employee in employees:
        employee.pay(date(2017, 9, 30))

    for e in employees:
        print(e.get_monthly_payment())

