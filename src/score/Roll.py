from src.score.Scorable import Scorable

class Roll(Scorable):
    def __init__(self, pins: int):
        self.pins = pins

    def calculate_score(self) -> int:
        return self.pins