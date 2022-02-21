"""
Question (12 marks)

TO HAND IN: Add your code to this file and hand it in on MarkUs.  Be sure to
run the self-test on MarkUs to avoid failing all our tests due to a silly error.
--------------------------------------------------------------------------------
In this question, you will write code to implement toys so that
the doctest examples below run without error, and these specifications are
followed:
- There are 2 kinds of toy for now, but we plan to add more later.
- All toys have a description and a lifespan.
- When any toy is played with, its lifespan decreases according to how long it
  was played with.  Its lifespan can go to zero, but not below (see example
  usage in the doctests below).
- If a toy's lifespan is at zero, it can't be played with any more.
- Repairing a toy adds back to its lifespan. The new value can even surpass its
  original lifespan.
- Trains have an initial lifespan of 20 units, and for dolls it is 15 units.
- A train has individual train cars, and we represent each of these simply by
  a string. We can index into a train to access the cars (see example usage
  in the doctests below). You may assume that the index will be valid.
- A doll has hair of a certain length.  When its hair is cut, the length of its
  hair decreases. If we ask to cut more hair than the doll has, nothing happens.
- All toys can return a string that is suitable for printing, but they each
  return something different, as shown below.
- You may assume that all integer arguments are > 0.
Any behaviour that is not specified by this description plus the doctests is
up to you.

We have started the code for you.
- You must not alter anything that is already written. Just add to it.
- No docstrings are required. But for full marks, you must provide type
  annotations that specify the return type and parameter types for each method.
- Part of the marks will be for avoiding repeated code where appropriate.
- Do not add any new attributes.

HINT: Run this module to check your code against these doctest examples:

>>> t1 = Train('Train set model 711', ['engine', 'tanker', 'boxcar', \
'caboose'])
>>> print(t1)
Train set model 711 with 4 cars and remaining lifespan 20
>>> print(t1[2])
boxcar
>>> t1.play(3)
That was fun!
>>> print(t1)
Train set model 711 with 4 cars and remaining lifespan 17
>>> d1 = Doll('Victorian doll', 80)
>>> print(d1)
Victorian doll with remaining lifespan 15 and hair length 80
>>> d1.play(12)
That was fun!
>>> print(d1)
Victorian doll with remaining lifespan 3 and hair length 80
>>> d1.cut_hair(50)
>>> print(d1)
Victorian doll with remaining lifespan 3 and hair length 30
>>> d1.cut_hair(50)   # Can't be done -- there isn't enough hair left!
>>> print(d1)
Victorian doll with remaining lifespan 3 and hair length 30
>>> d1.repair(20)
>>> print(d1)
Victorian doll with remaining lifespan 23 and hair length 30
>>> d1.play(5)
That was fun!
>>> print(d1)
Victorian doll with remaining lifespan 18 and hair length 30
>>> d1.play(25)   # This brings lifespan to 0; it can't go lower.
That was fun!
>>> print(d1)
Victorian doll with remaining lifespan 0 and hair length 30
>>> d1.play(1)
Sorry, I am broken and cannot play


--------------------------------------------------------------------------------
This file is Copyright (c) 2022 University of Toronto
All forms of distribution, whether as given or with any changes, are
expressly prohibited.
--------------------------------------------------------------------------------
"""
from __future__ import annotations
from typing import List


class Toy:
    description: str
    lifespan: int

    def __init__(self, description: str, lifespan: int) -> None:
        self.description = description
        self.lifespan = lifespan
    """
    def play(self, time_played: int) -> str:
        if self.lifespan == 0:
            print('Sorry I am broken and cannot play')
            return None
        self.lifespan = self.lifespan - time_played
        if self.lifespan < 0:
            self.lifespan = 0
        else:
            self.lifespan -= time_played
        print('That was fun!')
    """
    def play(self, time_played: int) -> str:
        if self.lifespan == 0:
            print('Sorry, I am broken and cannot play')
        else:
            self.lifespan -= time_played
            if self.lifespan < 0:
                self.lifespan = 0
            print('That was fun!')

    def repair(self, repair: int) -> None:
        self.lifespan += repair


class Train(Toy):
    description: str
    lifespan: int
    cars: List[str]

    def __init__(self, description: str, train_cars: list[str]) -> None:
        Toy.__init__(self, description, 20)
        self.cars = train_cars

    def __str__(self) -> str:
        return f'{self.description} with {len(self.cars)} cars and ' \
               f'remaining lifespan {self.lifespan}'

    def __getitem__(self, item: int) -> str:
        return self.cars[item]


class Doll(Toy):
    description: str
    lifespan: int
    hair: int

    def __init__(self, description: str, hair: int) -> None:
        Toy.__init__(self, description, 15)
        self.hair = hair

    def __str__(self):
        return f'{self.description} with remaining lifespan {self.lifespan} ' \
               f'and hair length {self.hair}'

    def cut_hair(self, cut: int) -> None:
        if self.hair - cut > 0:
            self.hair -= cut


if __name__ == '__main__':
    import doctest
    doctest.testmod()
