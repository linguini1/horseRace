# Die class for rolling dice
__author__ = "Matteo Golin"

# Imports
import random

# Constants
SIDES = 6

# Class
class Die:

    def __init__(self, sides: int = SIDES) -> None:
        self.sides: int = sides

    def roll(self) -> int:

        """Returns the result of the die roll as an integer."""

        return random.choice(range(0, SIDES)) + 1

