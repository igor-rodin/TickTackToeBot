import enum


class BotMode(enum.Enum):
    DUMMY = 1
    SMART = 2


class GameState(enum.Enum):
    BOT_MODE = 1
    START_TURN = 2
    USER_TURN = 3
