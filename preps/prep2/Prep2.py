from __future__ import annotations


class HockeyTeam:
    """A hockey team in a league

    === Attributes ===
    name: the name of this team
    games_played: number of games this team has played
    wins: the number of games this team has won
    """
    name: str
    games_played: int
    wins: int

    def __init__(self, name: str) -> None:
        """Initialize this hockey team, with no games played yet.
        """
        self.name = name
        self.games_played = 0
        self.wins = 0

    def record_result(self, result: str) -> None:
        """Record a win/loss from a game.

        Precondition: result == 'W' or result == 'L'
        """
        self.games_played += 1
        if result == 'W':
            self.wins += 1


class Person:
    """A person
    === Attributes ===
    name: name of the person
    age: age of the person in years
    mood: mood throughout the day
    fav_food: favourite food
    """
    name: str
    age: int
    mood: str
    fav_food: str

    def __init__(self, name: str, age: int, mood: str, fav_food: str):
        """Initialise this person, with respective name, age, mood and favourite
        food
        """
        self.name = name
        self.age = age
        self.mood = mood
        self.fav_food = fav_food

    def eat_fav_food(self, food_eaten: str):
        """Change Person's mood to ecstatic if their favourite food is eaten

        >>> Sally = Person('Sally', 23, 'sad', 'cheetos')
        >>> Sally.mood
        'sad'
        >>> Sally.eat_fav_food('apples')
        >>> Sally.mood
        'sad'
        >>> Sally.eat_fav_food('cheetos')
        >>> Sally.mood
        'ecstatic'
        """
        if food_eaten == self.fav_food:
            self.mood = 'ecstatic'

    def change_name(self, new_name: 'str'):
        self.name = new_name

    def greeting(self, other_person: Person):
        """Greet other_person with the phrase 'Hi ____, it's nice to meet you!
        I'm ____.'
        """
        return "Hi {0}, it's nice to meet you! I'm {1}.".format(
            other_person.name,
            self.name)


class Rational:
    """A rational number class that gives a numerator and a denominator as
    values to be implemented and used

    === Attributes ===
    numerator: int
    denominator: int

    Precondition: denominator cannot be 0
    """
    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Precondition: Denominator cannot be 0
        """
        self.numerator = numerator
        self.denominator = denominator

    def is_positive(self) -> bool:
        """Determines whether the given rational number is positive or negative

        >>> fraction = Rational(1, 2)
        >>> fraction.is_postive()
        True

        >>> fraction = Rational(-1, 4)
        >>> fraction.is_positive()
        False
        """
        return self.numerator > 0

    def __str__(self) -> str:
        """Return a rational number in the form of the string:
        'numerator/denominator

        >>> rational_1 = Rational(7, 12)
        >>> print(rational_1)
        '7/12'

        >>> rational_2 = Rational(8. 19)
        >>> print(rational_2)
        '8/19'
        """
        return str(self.numerator) + '/' + str(self.denominator)

    def add(self, other: Rational) -> str:
        """Add two rational numbers together and return the result as a
        simplified rational number that is a string

        >>> first_number = Rational(1, 2)
        >>> second_number = Rational(7, 8)
        >>> first_number.add(second_number)
        11/8
        """
        final_denominator = self.denominator * other.denominator
        numerator_1 = other.denominator * self.numerator
        numerator_2 = other.numerator * self.denominator
        final_numerator = numerator_1 + numerator_2

        i = 2
        while not final_numerator % i == 0 and final_denominator % i == 0:
            i += 1
        return str(final_numerator // i) + '/' + str(final_denominator // i)

    def multiply(self, other: Rational) -> str:
        """Multiply two rational numbers together and return the result as a
        string

        >>> rational_1 = Rational(1, 2)
        >>> rational_2 = Rational(6, 9)
        >>> rational_1.multiply(rational_2)
        '6/18'
        """
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return str(new_num) + '/' + str(new_den)


class RaceReg:
    """

    """

