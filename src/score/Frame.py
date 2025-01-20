from score.Scorable import Scorable
from score.Roll import Roll
from score.FrameStatus import FrameStatus

class Frame(Scorable):
    def __init__(self):
        self.rolls: list[Roll] = []
        self.score: int = 0
        self.bonus: int = 0
        self.status: str = FrameStatus.NORMAL

    def calculate_score(self) -> int:
        return self.score + self.bonus

    def get_roll_scores(self) -> list[int]:
        return [roll.calculate_score() for roll in self.rolls]

    def add_roll(self, pins: int) -> None:
        self.rolls.append(Roll(pins))
        self.score += pins
    
    def add_bonus(self, bonus: int):
        self.bonus += bonus

    # Calculates bonuses for adding to previous frames
    def calculate_bonus(self, status):
        if status == FrameStatus.STRIKE:
             return sum([roll.calculate_score() for roll in self.rolls[0:2]])
        elif status == FrameStatus.SPARE:
            return self.rolls[0].calculate_score()
        else:
            return 0

    def set_status(self) -> None:
        if self.rolls[0].calculate_score() == 10:
            self.status = FrameStatus.STRIKE
        elif len(self.rolls) == 2 and sum([roll.calculate_score() for roll in self.rolls]) == 10:
            self.status = FrameStatus.SPARE
    
    def get_status(self) -> str:
        return self.status

    def has_ended(self) -> bool:
        return len(self.rolls) == 2 or (len(self.rolls) == 1 and self.rolls[0].calculate_score() == 10)