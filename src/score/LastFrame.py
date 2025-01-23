from score.Frame import Frame
from score.enums.FrameStatus import FrameStatus

class LastFrame(Frame):
    def has_ended(self) -> bool:
        return len(self.rolls) == 3 or (len(self.rolls) == 2 and self.score < 10)
    
    def wrap_it_up(self) -> int:
        bonus = self.calculate_last_frame_bonus()
        self.bonus = bonus
        self.score -= bonus

        if self.status == FrameStatus.STRIKE:
            del self.rolls[-2:]
        elif self.status == FrameStatus.SPARE:
            del self.rolls[-1:]
        
        return bonus
        
    def calculate_last_frame_bonus(self) -> None:
        if self.status == FrameStatus.STRIKE or self.status == FrameStatus.SPARE:
            return self.score - 10
        
        return 0