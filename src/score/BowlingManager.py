from src.score.Player import Player
from src.score.Frame import Frame
from src.score.enums.GameStatus import GameStatus


class BowlingManager:
    """
    Manages the flow of a bowling game, including players, frames, and scores.

    Attributes:
        players (list[Player]): The players participating in the game.
        current_player (int): The index of the player whose turn it is.
        game_status (GameStatus): The overall status of the game.
    """

    def __init__(self, players: list[Player]) -> None:
        """
        Initializes the BowlingManager with a list of players.

        Args:
            players (list[Player]): the players of the game
        """
        if not players:
            raise ValueError("At least one player is needed to start the game.")
        self.players: Player = players
        self.current_player: int = 0
        self.game_status: GameStatus = GameStatus.ONGOING

    def play(self, pins: int) -> None:
        """
        Calls the play() method of the current player, for the closure of
        its current frame and calls for the turn to be updated to
        the next player (if needed).

        Args:
            pins (int): the number of pins hit in the roll
        """
        current_player = self.players[self.current_player]
        if current_player.game_status != GameStatus.ONGOING:
            self.__next_turn()

        current_player.play(pins)
        if current_player.current_frame_has_ended():
            current_player.end_frame()
            self.__next_turn()

    def get_current_frame_remaining_pins(self) -> int:
        """Calculates the remaining pins of the active frame of the current player."""
        return self.players[self.current_player].get_current_frame_remaining_pins()

    def calculate_player_score(self) -> int:
        """Calculates the score of the current player."""
        return self.players[self.current_player].calculate_score()

    def get_current_player(self) -> Player:
        """Returns the current player"""
        return self.players[self.current_player]

    def game_has_ended(self) -> bool:
        """
        Checks if the game has ended, i.e., if the game_status is not
        'ongoing' for every player.
        """
        return all(
            [player.game_status != GameStatus.ONGOING for player in self.players]
        )

    def __next_turn(self) -> None:
        """Passes the turn to the next player"""
        self.current_player = (
            self.current_player + 1
            if self.current_player < (len(self.players) - 1)
            else 0
        )
