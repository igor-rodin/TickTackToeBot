from random import choice
import botai as bai
import tictactoe_model as toe


def converter(val: str) -> str:
    if val.isdigit():
        return val
    return toe.sym_dict[val]


def list2str(moves: list):
    new_m = tuple(map(converter, moves))
    return "".join(new_m)


def get_bot_turn(moves: list, sym: str, mode=2) -> int:
    if mode == 1:
        return get_dummy_turn(moves)
    elif mode == 2:
        return get_rand_turn(moves)
    else:
        free_moves = tuple(filter(str.isdigit, moves))
        res = int(bai.get_bot_turn(list2str(moves), toe.sym_dict[sym], mode))
        while moves[res - 1] not in free_moves:
            res = int(bai.get_bot_turn(
                list2str(moves), toe.sym_dict[sym], mode))
        return res - 1


def get_dummy_turn(moves: list) -> int:
    free_moves = tuple(filter(str.isdigit, moves))

    return int(free_moves[0]) - 1


def get_rand_turn(moves: list) -> int:
    free_moves = tuple(filter(str.isdigit, moves))

    return -1 if len(free_moves) == 0 else int(choice(free_moves)) - 1
