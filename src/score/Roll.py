from src.score.Scorable import Scorable


class Roll(Scorable):
    """
    Represents a single roll in a bowling game.

    A roll tracks the number of pins knocked down and provides functionality
    to calculate its score.

    Attributes:
        pins (int): The number of pins hit in this roll.
    """

    def __init__(self, pins: int):
        """
        Initializes a new roll.

        Args:
            pins (int): The number of pins hit in the roll.
        """
        self.pins = pins

    def calculate_score(self) -> int:
        """Returns the number of pins hit in the roll."""
        return self.pins
