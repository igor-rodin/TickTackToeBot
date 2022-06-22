from random import choice
import botai as bai
import tictactoe as toe


def converter(val: str) -> str:
    if val.isdigit:
        return val
    return toe.sym_dict[val]


def list2str(moves: list):
    new_m = tuple(map(converter, moves))
    return "".join(new_m)


def get_bot_turn(moves: list, sym: str, mode=2) -> int:
    if mode == 2:
        return get_rand_turn(moves)
    else:
        return bai.get_bot_turn(list2str(moves), toe.sym_dict[sym], mode)


def get_rand_turn(moves: list) -> int:
    free_moves = tuple(filter(str.isdigit, moves))

    return -1 if len(free_moves) == 0 else int(choice(free_moves)) - 1


mv = ['1', '2', '⭕', '4', '❌']
l = list2str(mv)
print(l)
