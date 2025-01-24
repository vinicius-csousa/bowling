from src.score.Scorable import Scorable
from src.score.Frame import Frame
from src.score.LastFrame import LastFrame
from src.score.enums.FrameStatus import FrameStatus
from src.score.enums.GameStatus import GameStatus

class Player(Scorable):
    def __init__(self, name: str):
        self.name = name
        self.frames: list[Frame] = []
        self.current_frame = Frame()
        self.bonus_list: list[dict[str, int]] = []
        self.game_status: GameStatus = GameStatus.ONGOING

    def calculate_score(self) -> int:
        return sum([frame.calculate_score() for frame in self.frames])
    
    def play(self, pins: int) -> bool:
        self.current_frame.play(pins)
        self.add_bonus(pins)
        
        if self.current_frame.has_ended():
            self.end_frame()
            return True
        
        return False

    def end_frame(self) -> None:
        self.add_to_bonus_list(self.current_frame.status)
        self.frames.append(self.current_frame)

        number_of_frames = len(self.frames)
        if number_of_frames < 9:
            self.current_frame = Frame()
        elif number_of_frames == 9:
            self.current_frame = LastFrame()
        elif number_of_frames == 10:
            self.current_frame.wrap_it_up()
            self.set_game_status()
        else:
            return
    
    def add_to_bonus_list(self, status) -> None:
        if len(self.frames) == 10:
            return

        bonus_rolls = 2 if status == FrameStatus.STRIKE else 1 if status == FrameStatus.SPARE else 0
        if bonus_rolls > 0:
              self.bonus_list.append({"frame_index": len(self.frames), "bonus_rolls": bonus_rolls})

    def add_bonus(self, pins: int) -> None:
        self.bonus_list = [
            {**element, "bonus_rolls": element["bonus_rolls"] - 1}
            for element in self.bonus_list
            if self.frames[element["frame_index"]].add_bonus(pins) or element["bonus_rolls"] > 1
    ]

    def set_game_status(self) -> None:
        score = self.calculate_score()
        if score == 300:
            self.game_status = GameStatus.PERFECT_GAME
        elif score == 0:
            self.game_status = GameStatus.GUTTER_GAME
        else:
            self.game_status = GameStatus.FINISHED

    def get_frames(self) -> list[Frame]:
        if len(self.frames) < 10 and len(self.current_frame.rolls) == 1:
            return self.frames + [self.current_frame]
        return self.frames