from score.Scorable import Scorable
from score.Player import Player

class Score(Scorable):
    def __init__(self, ):
        self.players: list[Player] = []
        
    def calculate_score(self, player: Player) -> int:
        return player.calculate_score()
