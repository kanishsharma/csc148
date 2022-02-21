"""Catching exceptions

=== Copyright information ===
CSC148
Department of Computer Science
University of Toronto

=== Module description ===
This module demonstrates the basics of 'catching' and dealing with exceptions,
rather than letting them clear the stack and report a nasty error message to
the user.

It is possible to end with a 'bare' except clause, that is, one with no
specific type of exception named.  This is similar to a final else clause
with no condition.  While fine for if-statements, this is considered bad style
for exceptions.

Try running this and giving an integer as input, then run it with "bad" input.
What does the user see?
"""

def f3() -> None:
    # The 'try' says to Python: Go ahead and try running the code inside
    # this block.  But if an error is raised, (1) jump immediately to the
    # first 'except', (2) find the first 'except' clause that matches the
    # error (3) do what is in its block, and (4) carry on with the
    # program.
    try:
        x = input('Enter a number: ')
        print(100 / int(x))
        print('That went well')
    except ZeroDivisionError:
        print('Do not divide by zero!')
    except ValueError:
        print('That was not a number!')
    print('Okay, let\'s continue with this program')


def f2() -> None:
    f3()


def f1() -> None:
    f2()


if __name__ == '__main__':
    f1()
    print('All done.')
