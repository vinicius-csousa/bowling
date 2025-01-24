from enum import Enum

class Status(Enum):
    NOT_STARTED = 'not_started'
    ROLLLING = 'rolling'
    STANDBY = 'standby'
    GAME_ENDED = 'game_ended'