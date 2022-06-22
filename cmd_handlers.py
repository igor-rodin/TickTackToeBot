from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from menu import create_choose_menu
from const import GameState


def start(update: Update, context: CallbackContext):
    welcome_msg = " <b>TicTac4Bot</b> - простой бот для игры в крестики-нолики с ИИ \nКоманды:\n \
                <i>/new_game</i> - Начало новой игры"
    update.message.reply_text(
        text=welcome_msg, parse_mode=ParseMode.HTML)


def new_game(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    msg = f"\tПривет, {user}! \nВыберите правильную сторону..."
    # X - U+274C
    # O - U+2B55
    comands = ['❌', '⭕']
    menu = create_choose_menu(comands)
    update.message.reply_text(text=msg, reply_markup=menu)
    return GameState.FIRST_TURN


def turn(update: Update, context: CallbackContext):
    pass


def end_game(update: Update, context: CallbackContext):
    pass


def select(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        f"Ваш выбор: {query.data}\n Начинаем ...")
