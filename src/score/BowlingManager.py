from score.Player import Player
from score.enums.GameStatus import GameStatus

class BowlingManager():
    def __init__(self, players: list[Player]):
        if not players:
            raise ValueError("At least one player is needed to start the game.")
        self.players: Player = players
        self.current_player: int = 0
        self.game_status: GameStatus = GameStatus.ONGOING
        
    def calculate_player_score(self, player_index: int) -> int:
        return self.players[player_index].calculate_score()
    
    def play(self, pins: int) -> None:
        current_player = self.players[self.current_player]
        
        if current_player.game_status == GameStatus.ONGOING:
            self.next_turn(current_player.play(pins))
            return
        self.next_turn(True)

    def next_turn(self, frame_has_ended) -> None:
        if frame_has_ended:
            self.current_player = self.current_player + 1 if self.current_player < (len(self.players) - 1) else 0

    def has_ended(self):
        return all([player.game_status != GameStatus.ONGOING for player in self.players])
