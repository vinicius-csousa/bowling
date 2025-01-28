from enum import Enum


class GameStatus(Enum):
    """
    An Enum for representing the possible game statuses in a
    bowling game.
    """

    ONGOING = "ongoing"
    FINISHED = "finished"
    GUTTER_GAME = "gutter_game"
    PERFECT_GAME = "perfect_game"
