from score.Frame import Frame
from score.FrameStatus import FrameStatus

class LastFrame(Frame):
    def has_ended(self) -> bool:
        number_of_rolls = len(self.rolls)
        return number_of_rolls == 3 or (number_of_rolls == 2 and self.score < 10)
    
    def wrap_it_up(self) -> int:
        bonus = self.calculate_last_frame_bonus()
        self.bonus += bonus

        if self.status == FrameStatus.STRIKE:
            del self.rolls[-2:]
        elif self.status == FrameStatus.SPARE:
            del self.rolls[-1:]
        
        return bonus
        
    def calculate_last_frame_bonus(self):
        if self.status == FrameStatus.STRIKE or self.status == FrameStatus.SPARE:
            return self.score - 10
        else:
            return 0