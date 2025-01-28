from src.score.Player import Player
from src.score.Frame import Frame
from src.score.LastFrame import LastFrame
from src.score.enums.FrameStatus import FrameStatus


def get_integer_input(prompt: str, min_value: int, max_value: int) -> int:
    """
    Prompts the user for an integer input within a specified range.

    The function repeatedly prompts the user until a valid integer is entered.

    Args:
        prompt (str): The message to display to the user.
        min_value (int): The minimum valid value.
        max_value (int): The maximum valid value.

    Returns:
        int: A valid integer input from the user.
    """
    while True:
        try:
            input_value = int(input(prompt))
            if min_value <= input_value <= max_value:
                return input_value
            print(f"Input must be between {min_value} and {max_value}.")
        except ValueError:
            print("Input must be an integer.")


def get_string_input(prompt: str, max_len: int) -> str:
    """
    Prompts the user for a valid string input.

    The function repeatedly prompts the user until a valid string is entered.

    Args:
        prompt (str): The message to display to the user.
        max_len (int): The maximum number of characters allowed.
    Returns:
        str: A valid string input from the user.
    """
    while True:
        input_string = input(prompt)
        if 1 <= len(input_string) <= max_len:
            return input_string
        print(f"Input must have between {1} and {max_len} characters.")


def print_scorecard(player: Player):
    """
    Prints the scorecard for a given player, displaying rolls and cumulative scores.

    Args:
        player (Player): The player whose scorecard is to be displayed.
    """
    print(f"Player: {player.name}")

    # Top border
    print("+----" * 10 + "+")

    # Rolls (inside frames)
    roll_line = ""
    for frame in player.get_frames():
        roll_line += f"|{format_rolls(frame):4}"
    roll_line += "|"
    print(roll_line)

    # Separator
    print("+----" * 10 + "+")

    # Cumulative scores (below rolls)
    cumulative_scores = calculate_cumulative_scores(player)
    score_line = ""
    for score in cumulative_scores:
        score_line += f"|{score:4}" if score is not None else "|    "
    score_line += "|"
    print(score_line)

    # Bottom border
    print("+----" * 10 + "+\n")


def format_rolls(frame: Frame) -> str:
    """
    Formats the rolls for a given frame into a string for display.

    Handles both regular frames and the special rules for the 10th frame.

    Args:
        frame (Frame): The frame whose rolls are to be formatted.

    Returns:
        str: A string representation of the rolls in the frame.
    """
    rolls = frame.get_rolls()

    # Handle 10th frame
    if isinstance(frame, LastFrame):
        return format_last_frame_rolls(rolls)

    # Handle regular frames
    if frame.status == FrameStatus.STRIKE:
        return " X  "  # Strike
    elif frame.status == FrameStatus.SPARE:
        return f"{rolls[0]} /"  # Spare
    else:
        # Open frame: Display both rolls or the first roll if incomplete
        if len(rolls) == 2:
            return f"{rolls[0]} {rolls[1]}"
        elif len(rolls) == 1:
            return f"{rolls[0]}   "  # Single roll
        else:
            return "    "  # Empty frame


def format_last_frame_rolls(rolls: list[int]) -> str:
    """Format rolls of the 10th frame for display."""
    result = []
    for i, roll in enumerate(rolls):
        if roll == 10:
            result.append("X")  # Strike
        elif i > 0 and sum(rolls[i - 1 : i + 1]) == 10:
            result.append("/")  # Spare
        else:
            result.append(str(roll))  # Normal roll

    return " ".join(result).ljust(5)  # Ensure consistent spacing


def calculate_cumulative_scores(player: Player) -> list[int | None]:
    """
    Calculates the cumulative scores for each frame played by the player.

    If the game is ongoing, pads the remaining frames with None.

    Args:
        player (Player): The player whose cumulative scores are to be calculated.

    Returns:
        list[int | None]: A list of cumulative scores for each frame. Unfinished frames are None.
    """
    cumulative = []
    total = 0

    for frame in player.frames:
        total += frame.calculate_score()
        cumulative.append(total)

    # If the game is ongoing, pad the remaining frames with None
    for _ in range(10 - len(cumulative)):
        cumulative.append(None)

    return cumulative
