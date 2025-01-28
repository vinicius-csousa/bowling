from src.score.BowlingManager import BowlingManager
from src.score.enums.GameStatus import GameStatus
from src.helpers.helpers import get_integer_input, print_scorecard


class BowlingGameEngine:
    """
    Handles the flow of a bowling game, interacting with the BowlingManager
    to process turns, display game status, and handle user inputs.

    Attributes:
        manager (BowlingManager): The manager that controls the state and logic of the bowling game.
    """

    def __init__(self, manager: BowlingManager):
        """Initializes the BowlingGameEngine instance with a BowlingManager."""
        self.manager = manager

    def play(self) -> None:
        """Gets inputs for plays and passes them to the bowling manager."""
        current_player = self.manager.get_current_player()
        print(
            f"{current_player.name}'s turn on frame {len(current_player.get_frames())}: \n"
        )

        pins = self.__get_roll_input(self.manager.get_current_frame_remaining_pins())
        self.manager.play(pins)

    def game_has_ended(self) -> bool:
        """Checks if the game has ended according to the bowling manager."""
        return self.manager.game_has_ended()

    def display_game_status(self) -> None:
        """Prints scorecards for each player."""
        for player in self.manager.players:
            print_scorecard(player)

    def show_final_results(self) -> None:
        """Shows an ordered scoreboard of the players at the end of the game."""
        print("The game has ended! Here are the final results:\n")
        self.display_game_status()
        print("Scoreboard:\n")
        scores = sorted(
            [
                (player.name, player.calculate_score(), player.game_status)
                for player in self.manager.players
            ],
            key=lambda x: x[1],
            reverse=True,
        )
        for i, (name, score, game_status) in enumerate(scores, start=1):
            line = f"{i}. {name}: {score} points"
            if game_status == GameStatus.GUTTER_GAME:
                line += " - Gutter Game!"
            if game_status == GameStatus.PERFECT_GAME:
                line += " - Perfect Game!"
            print(line)
        print("\n")

    def __get_roll_input(self, remaining_pins: int) -> int:
        """Gets integer inputs for rolls (respecting the number of pins remaining) and returns them."""
        return get_integer_input(
            f"Enter pins knocked down (0-{remaining_pins}): ", 0, remaining_pins
        )
