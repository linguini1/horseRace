# Writes statistics to a JSON file
__author__ = "Matteo Golin"

# Imports
import json
import os

# Constants
FILE_NAME: str = "stats.json"

# Class
class Stats:

    def __init__(self) -> None:
        self.data = self.__load_data()

    def __load_data(self) -> dict:

        """Loads the statistic data from previous rounds."""

        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                data = json.load(file)
        
        else:
            data = {}
            for _ in range(2, 13):
                data[str(_)] = {
                    "wins": 0,
                    "debts": 0
                }

        return data

    def write_results(self, results: dict) -> None:

        """Writes the round's results to the stats object."""

        # Winner
        winner = str(results["winner"])
        self.data[winner]["wins"] += 1

        # Debt
        for horse in results["debt"]:
            self.data[str(horse)]["debts"] += 1
        
    def save(self) -> None:

        """Saves the results to the file."""

        with open(FILE_NAME, 'w') as file:
            json.dump(self.data, file)
        
