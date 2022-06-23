from math import sqrt
from random import choice

symbols = ('❌', '⭕')
sym_dict = {'❌': 'X', '⭕': 'O'}
mode_dict = {1: 'Dummy', 2: 'Random', 3: 'MegaBrain'}


def init_board(size=3):
    return [str(i) for i in range(1, size**2 + 1)]


def check_winers(moves: list, cur_sym: str, choice: int) -> bool:
    size = int(sqrt(len(moves)))
    row = choice // int(sqrt(len(moves)))
    col = choice - row * int(sqrt(len(moves)))

    main_diag = moves[::size + 1].count(cur_sym)
    ad_diag = moves[size - 1:-2:size - 1].count(cur_sym)
    hor = moves[row * size:row * size + size].count(cur_sym)
    vert = moves[col:col + 2 * size + 1:size].count(cur_sym)
    if main_diag == size or ad_diag == size or hor == size or vert == size:
        return True

    return False


def has_turns(moves: list) -> int:
    free_moves = tuple(filter(str.isdigit, moves))

    return len(free_moves) != 0


def get_first_turn(syms: tuple):
    return choice(syms)
