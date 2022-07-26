# Game class to control the rounds
__author__ = "Matteo Golin"

# Imports
from classes.horse import Horse
from classes.die import Die
from classes.stats import Stats

# Constants
SPACING = [2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2]


# Class
class Game:

    def __init__(self, rounds: int) -> None:
        self.rounds: int = rounds
        self.horses = self.__create_horses()
        self.dice = (Die(), Die())
        self.stats = Stats()

    @staticmethod
    def __create_horses() -> dict[int, Horse]:

        """
        Returns the horse pieces for the game in a dict where the key
        is the value of the horse.
        """

        horses = {}

        for val, space in zip(range(2, 13), SPACING):
            horses[val] = Horse(val, space)

        return horses

    def __roll_dice(self) -> int:

        """Returns the sum of both the dies' roll."""

        sum = 0
        for die in self.dice:
            sum += die.roll()

        return sum

    def __set_debt_horses(self) -> None:

        """Plays the first four rounds to determine which horses are in debt."""

        count = 0
        while count != 4:  # Four horses must be in debt

            dice_roll = self.__roll_dice()
            rolled_horse = self.horses.get(dice_roll)

            if not rolled_horse.in_debt:
                rolled_horse.in_debt = True
                count += 1

    def _play_turn(self) -> None:

        """Advances the game by one turn."""

        dice_roll = self.__roll_dice()
        rolled_horse = self.horses.get(dice_roll)

        if not rolled_horse.in_debt:
            rolled_horse.move_up()

    def _play_round(self) -> dict:

        """Returns the results of the game."""

        # Set horses in debt
        self.__set_debt_horses()

        # Play until a horse has won
        while not any([horse.has_won for horse in self.horses.values()]):
            self._play_turn()

        # Find the winning horse and horses in debt
        results = {
            "winner": None,
            "debt": []
        }
        
        for horse in self.horses.values():
            
            if horse.has_won:
                results["winner"] = horse._value
            
            elif horse.in_debt:
                results["debt"].append(horse._value)

        return results


    def run_game(self) -> None:

        """Runs all the rounds and stores results."""

        for _ in range(self.rounds):

            # Collect stats
            results = self._play_round()
            self.stats.write_results(results)

            # Reset
            for horse in self.horses.values():
                horse.reset()
        
        self.stats.save()

