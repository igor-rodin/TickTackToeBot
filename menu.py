from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)


def create_mode_menu(dict_mode: dict) -> InlineKeyboardMarkup:

    menu_layot = [[InlineKeyboardButton(
        dict_mode[val], callback_data=str(val)) for val in (1, 2, 3)]]
    return InlineKeyboardMarkup(menu_layot, resize_keyboard=True)


def create_choose_menu(comands: list) -> InlineKeyboardMarkup:
    menu_layot = [[InlineKeyboardButton(
        val, callback_data=val) for val in comands]]

    return InlineKeyboardMarkup(menu_layot, resize_keyboard=True)


def create_board(moves: list, size=3) -> list:
    board = [[InlineKeyboardButton(moves[i + j * size], callback_data=moves[i + j * size]) for i in range(size)]
             for j in range(size)]

    return InlineKeyboardMarkup(board, resize_keyboard=True)
