from enum import Enum


class FrameStatus(Enum):
    """
    An Enum for representing the possible frame statuses in a
    bowling game.
    """

    ONGOING = "ongoing"
    FINISHED = "finished"
    STRIKE = "strike"
    SPARE = "spare"
