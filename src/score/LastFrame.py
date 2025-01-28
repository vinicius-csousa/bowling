from src.score.Frame import Frame
from src.score.enums.FrameStatus import FrameStatus


class LastFrame(Frame):
    """
    The last frame of a bowling game.

    Differs from a regular frame as it can have up to three rolls (depending on strikes or spares).
    """

    def has_ended(self) -> bool:
        """
        Checks if the last frame has ended, which can happen when:
            - there are three rolls in the frame
            - there are only two rolls, but the score is lower than 10 (not a strike nor
            a spare, so no right to a third roll)
        """
        return len(self.rolls) == 3 or (len(self.rolls) == 2 and self.score < 10)

    def get_remaining_pins(self) -> int:
        """
        Calculates the remaining pins of the frame:
            - if there's a strike in the first or second rolls or a spare, gives a new full roll with 10 pins
            - if there's a strike in the first roll and a normal roll afterwards, returns the remaining pins
              (10 minus the ones hit in the second roll)
            - returns 10 minus the pins hit in the first roll, if none of the conditions above are met
        """
        num_rolls = len(self.rolls)

        if num_rolls == 1 and self.status == FrameStatus.STRIKE:
            return 10

        if num_rolls == 2:
            # If two strikes in the first two rolls or a spare
            if self.score == 20 or self.status == FrameStatus.SPARE:
                return 10
            elif self.score < 20:  # One strike then one normal roll
                return 10 - self.rolls[1].calculate_score()
        return 10 - self.score

    def wrap_it_up(self) -> None:
        """
        Manages the closing process of the last frame, i.e., adds the scores of
        the additional rolls to bonuses and removes them from the normal score
        """
        bonus = self.calculate_last_frame_bonus()
        self.bonus = bonus
        self.score -= bonus

    def calculate_last_frame_bonus(self) -> int:
        """
        Returns the bonuses of the last frame:
            - (score - 10) if the frame had a strike or a spare
            - zero, else
        """
        if self.status == FrameStatus.STRIKE or self.status == FrameStatus.SPARE:
            return self.score - 10

        return 0
