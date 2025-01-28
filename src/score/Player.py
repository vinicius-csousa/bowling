from src.score.Scorable import Scorable
from src.score.Frame import Frame
from src.score.LastFrame import LastFrame
from src.score.enums.FrameStatus import FrameStatus
from src.score.enums.GameStatus import GameStatus


class Player(Scorable):
    """
    Represents a player in a bowling game.

    Attributes:
        name (str): The name of the player.
        frames (list[Frame]): The frames completed by the player.
        current_frame (Frame): The player's current frame.
        bonus_list (list[dict[str, int]]): A list of bonuses yet to be applied, with the frame index
            and the number of bonus rolls remaining.
        game_status (GameStatus): The current game status of the player.
    """

    def __init__(self, name: str):
        """
        Initializes a new player.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.frames: list[Frame] = []
        self.current_frame = Frame()
        self.bonus_list: list[dict[str, int]] = []
        self.game_status: GameStatus = GameStatus.ONGOING

    def calculate_score(self) -> int:
        """
        Calculates the score of the player. If the game is still ongoing, considers the current frame, as
        it still hasn't been added to the frames list.

        Returns:
            int: The calculated score of the player
        """
        if len(self.frames) < 10:
            return (
                sum([frame.calculate_score() for frame in self.frames])
                + self.current_frame.calculate_score()
            )
        return sum([frame.calculate_score() for frame in self.frames])

    def play(self, pins: int) -> None:
        """Adds a roll to the current frame and call for bonus updates."""
        self.current_frame.play(pins)
        self.__add_bonus(pins)

    def current_frame_has_ended(self) -> bool:
        """Checks if the current frame of the player has ended."""
        return self.current_frame.has_ended()

    def end_frame(self) -> None:
        """
        Manages the closing process of the current frame:
            - adds it to the bonus list
            - adds the frame to the frames list
            - creates a new frame or calls for a game status update,
            in case all the frames have already been played.
        """
        self.__add_to_bonus_list(self.current_frame.status)
        self.frames.append(self.current_frame)

        number_of_frames = len(self.frames)
        if number_of_frames < 9:
            self.current_frame = Frame()
        elif number_of_frames == 9:
            self.current_frame = LastFrame()
        elif number_of_frames == 10:
            self.current_frame.wrap_it_up()
            self.__set_game_status()

    def get_current_frame_remaining_pins(self) -> int:
        """Calculates how many pins are remaining in the current frame."""
        return self.current_frame.get_remaining_pins()

    def __add_to_bonus_list(self, status: FrameStatus) -> None:
        """
        Adds a frame to the bonus list based on its status (strike or spare).

        The bonus list tracks frames that require additional rolls to calculate their final score.
        Each entry in the bonus list follows this structure:
            {
                "frame_index": int,  # The index of the frame to receive the bonus
                "bonus_rolls": int   # The number of bonus rolls required (2 for a strike, 1 for a spare)
            }

        Args:
            status (FrameStatus): The status of the frame (STRIKE, SPARE, or NORMAL).
        """
        if len(self.frames) == 10:
            return

        bonus_rolls = (
            2
            if status == FrameStatus.STRIKE
            else 1 if status == FrameStatus.SPARE else 0
        )
        if bonus_rolls > 0:
            self.bonus_list.append(
                {"frame_index": len(self.frames), "bonus_rolls": bonus_rolls}
            )

    def __add_bonus(self, pins: int) -> None:
        """
        Distributes bonus points to frames in the bonus list and updates the list.

        For each frame in the bonus list:
            - Adds the given number of pins to the frame as a bonus.
            - Decrements the number of remaining bonus rolls for that frame in the bonus list.
            - Removes the frame from the bonus list when all bonus rolls have been applied.

        Args:
            pins (int): The number of pins knocked down in the current roll, to be added as bonus points.
        """
        self.bonus_list = [
            {**element, "bonus_rolls": element["bonus_rolls"] - 1}
            for element in self.bonus_list
            if self.frames[element["frame_index"]].add_bonus(pins)
            or element["bonus_rolls"] > 1
        ]

    def __set_game_status(self) -> None:
        """Sets the game status at the end of the game."""
        score = self.calculate_score()
        if score == 300:
            self.game_status = GameStatus.PERFECT_GAME
            return
        elif score == 0:
            self.game_status = GameStatus.GUTTER_GAME
            return
        self.game_status = GameStatus.FINISHED

    def get_frames(self) -> list[Frame]:
        """Returns the frames of the player."""
        if len(self.frames) < 10:
            return self.frames + [self.current_frame]
        return self.frames
