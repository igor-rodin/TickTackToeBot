import enum


class BotMode(enum.Enum):
    DUMMY = 1
    SMART = 2


class GameState(enum.Enum):
    START_TURN = 1
    USER_TURN = 2
