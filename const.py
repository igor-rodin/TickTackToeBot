import enum


class GameState(enum.Enum):
    BOT_MODE = 1
    START_TURN = 2
    USER_TURN = 3
