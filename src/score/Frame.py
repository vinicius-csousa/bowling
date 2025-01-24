from src.score.Scorable import Scorable
from src.score.Roll import Roll
from src.score.enums.FrameStatus import FrameStatus

class Frame(Scorable):
    def __init__(self):
        self.rolls: list[Roll] = []
        self.score: int = 0
        self.bonus: int = 0
        self.status: FrameStatus = FrameStatus.NORMAL

    def calculate_score(self) -> int:
        return self.score + self.bonus

    def get_roll_scores(self) -> list[int]:
        return [roll.calculate_score() for roll in self.rolls]

    def play(self, pins: int) -> None:
        self.rolls.append(Roll(pins))
        self.score += pins

        self.set_status()
    
    def add_bonus(self, bonus: int):
        self.bonus += bonus

    def set_status(self) -> None:
        if self.rolls[0].calculate_score() == 10:
            self.status = FrameStatus.STRIKE
        elif len(self.rolls) == 2 and self.score == 10:
            self.status = FrameStatus.SPARE
        else:
            return

    def has_ended(self) -> bool:
        return len(self.rolls) == 2 or (len(self.rolls) == 1 and self.score == 10)