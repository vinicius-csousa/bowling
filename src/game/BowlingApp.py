import os
from src.game.BowlingGameEngine import BowlingGameEngine
from src.score.BowlingManager import BowlingManager
from src.score.Player import Player
from src.helpers.helpers import get_integer_input, get_string_input


class BowlingApp:
    """
    The entry point for running the bowling game application.
    Handles the initialization, game loop, and final results display.

    Attributes:
        bowling_engine (BowlingGameEngine): The engine that manages the game's logic and state.
    """

    def __init__(self):
        """Initializes the BowlingApp instance without starting the game."""
        self.bowling_engine = None

    def run(self) -> None:
        """
        Starts the bowling game application.

        This method clears the screen, initializes the game, runs the main game loop,
        and displays the final results.
        """
        self.__clear_screen()
        print("Welcome to the Bowling CLI Game!\n")
        self.__initialize_game()
        self.__game_loop()
        self.__show_final_results()

    def __clear_screen(self) -> None:
        """
        Clears the terminal screen to ensure a clean user interface.
        """
        os.system("cls") if os.name == "nt" else "clear"

    def __initialize_game(self) -> None:
        """
        Prompts the user to input the number of players and their names,
        then initializes the BowlingGameEngine with the players.
        """
        num_players = get_integer_input("Enter the number of players: ", 1, 2)

        players = []
        for i in range(num_players):
            players.append(
                Player(get_string_input(f"Enter the name of player {i + 1}: ", 20))
            )

        self.bowling_engine = BowlingGameEngine(BowlingManager(players))

    def __game_loop(self) -> None:
        """
        Runs the main game loop until the game has ended.

        The game loop repeatedly clears the screen, displays the current game status,
        and prompts the current player for their roll.
        """
        while not self.bowling_engine.game_has_ended():
            self.__clear_screen()
            self.bowling_engine.display_game_status()
            self.bowling_engine.play()

    def __show_final_results(self) -> None:
        """
        Clears the screen and displays the final results of the game,
        including player scores and rankings.
        """
        self.__clear_screen()
        self.bowling_engine.show_final_results()
