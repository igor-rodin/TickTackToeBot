from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)


def create_choose_menu(comands: list) -> InlineKeyboardMarkup:
    menu_layot = [[InlineKeyboardButton(
        val, callback_data=val) for val in comands]]

    return InlineKeyboardMarkup(menu_layot, resize_keyboard=True)
