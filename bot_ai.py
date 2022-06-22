from random import choice


def get_bot_turn(moves: list) -> int:
    free_moves = tuple(filter(str.isdigit, moves))

    return -1 if len(free_moves) == 0 else int(choice(free_moves)) - 1
