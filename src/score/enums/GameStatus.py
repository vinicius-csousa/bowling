from enum import Enum

class GameStatus(Enum):
    ONGOING = 'ongoing'
    FINISHED = 'finished'
    GUTTER_GAME = 'gutter_game'
    PERFECT_GAME = 'perfect_game'