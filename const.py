import enum


class BotMode(enum.Enum):
    DUMMY = 1
    SMART = 2


class GameState(enum.Enum):
    FIRST_TURN = 1
    SECOND_TURN = 2
