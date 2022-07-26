# Main run file
__author__ = "Matteo Golin"

# Imports
from classes.game import Game

# Main
def main():
    game = Game(10000)
    game.run_game()


if __name__ == "__main__":
    main()
