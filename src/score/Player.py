from score.Scorable import Scorable
from score.Frame import Frame
from score.LastFrame import LastFrame

class Player(Scorable):
    def __init__(self):
        self.frames: list[Frame] = []
        self.current_frame = Frame()
        self.score = 0

    def calculate_score(self) -> int:
        return self.score
    
    def play(self, pins: int) -> None:
        self.current_frame.add_roll(pins)
        self.score += pins
        self.current_frame.set_status()
        
        if self.current_frame.has_ended():
            self.update_frame()

    def update_frame(self) -> None:
        self.add_bonus()
        self.frames.append(self.current_frame)

        number_of_frames = len(self.frames)
        if number_of_frames < 9:
            self.current_frame = Frame()
        elif number_of_frames == 9:
            self.current_frame = LastFrame()
        elif number_of_frames == 10:
            self.score += self.current_frame.wrap_it_up()
        else:
            return

    def add_bonus(self) -> None:
        if not self.frames:
            return
        
        bonus = self.calculate_bonus()
        self.frames[len(self.frames) - 1].add_bonus(bonus)
        self.score += bonus

    def calculate_bonus(self) -> int:
        number_of_frames = len(self.frames)
        if number_of_frames > 9:
            return 0

        previous_frame_status = self.frames[number_of_frames- 1].get_status()
        return self.current_frame.calculate_bonus(previous_frame_status)

    def get_frames(self):
        return self.frames