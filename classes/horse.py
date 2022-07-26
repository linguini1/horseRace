# Horse class
__author__ = "Matteo Golin"


# Class
class Horse:

    """Represents horse pieces."""

    def __init__(self, value: int, spaces: int) -> None:
        self._value: int = value
        self.spaces: int = spaces
        self.position: int = 0
        self.in_debt: bool = False

    def move_up(self) -> None:

        """Increases the position of the horse."""

        self.position += 1

    @property
    def has_won(self) -> bool:

        """Returns true if the horse has travelled all of its spaces."""

        return self.spaces == self.position

    def reset(self) -> None:

        """Resets attributes for new game."""
        
        self.position = 0
        self.in_debt = False

    def __repr__(self):
        return f"{self._value}"
