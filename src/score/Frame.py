from src.score.Scorable import Scorable
from src.score.Roll import Roll
from src.score.enums.FrameStatus import FrameStatus


class Frame(Scorable):
    """
    Represents a single frame in a bowling game, including rolls and bonuses.

    A regular frame consists of up to two rolls.

    Attributes:
        rolls (list[Roll]): The rolls recorded for this frame.
        score (int): The total score for this frame, including bonuses.
        bonus (int): Additional points awarded for strikes and spares.
        status (FrameStatus): The current status of the frame (ongoing, finished, strike or spare).
    """

    def __init__(self):
        """
        Initializes a new empty frame.
        """
        self.rolls: list[Roll] = []
        self.score: int = 0
        self.bonus: int = 0
        self.status: FrameStatus = FrameStatus.ONGOING

    def calculate_score(self) -> int:
        """Calculate the score of the frame considering the bonus."""
        return self.score + self.bonus

    def get_rolls(self) -> list[int]:
        """Returns the roll scores of the current frame"""
        return [roll.calculate_score() for roll in self.rolls]

    def get_remaining_pins(self) -> int:
        """Calculates the remaining pins of the frame"""
        return 10 - self.score

    def play(self, pins: int) -> None:
        """
        Adds the roll to the frame and call for a status
        update
        """
        self.rolls.append(Roll(pins))
        self.score += pins
        self.__set_status()

    def add_bonus(self, bonus: int) -> None:
        """Adds bonuses to the frame."""
        self.bonus += bonus

    def has_ended(self) -> bool:
        """
        Check if the frame has ended, i.e. if its
        status is anything but 'ongoing'
        """
        return self.status != FrameStatus.ONGOING

    def __set_status(self) -> None:
        """
        Set the status of frame according to the
        score of its rolls
        """
        if self.rolls[0].calculate_score() == 10:
            self.status = FrameStatus.STRIKE
        elif len(self.rolls) == 2 and self.score == 10:
            self.status = FrameStatus.SPARE
        elif len(self.rolls) == 2 and self.score != 10:
            self.status = FrameStatus.FINISHED
        else:
            return
