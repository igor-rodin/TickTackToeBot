from telegram import Update, ParseMode
from telegram.ext import CallbackContext, ConversationHandler
from menu import create_choose_menu, create_board, create_mode_menu
from const import GameState
import tictactoe_model as tic
import bot_ai_wrap as ai


cur_sym = tic.symbols[0]
next_sym = tic.symbols[1]
bot_mode = 2
moves = tic.init_board


def start(update: Update, context: CallbackContext):
    welcome_msg = '''<b>TicTac4Bot</b> - простой бот для игры в крестики-нолики с ИИ
            Команды:
            <i>/new_game</i> - Начало новой игры
            <i>/end_game</i> - Завершить игру
            '''
    update.message.reply_text(
        text=welcome_msg, parse_mode=ParseMode.HTML)


def new_game(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    msg = f"\tПривет, {user}! \nВыберите интеллект бота..."

    mode_menu = create_mode_menu(tic.mode_dict)
    update.message.reply_text(text=msg, reply_markup=mode_menu)

    return GameState.BOT_MODE


def bot_mode(update: Update, context: CallbackContext):
    global bot_mode
    query = update.callback_query
    query.answer()
    bot_mode = int(query.data)

    msg = f"Вы выбрали уровень {tic.mode_dict[bot_mode]}\nТеперь выберите правильную сторону..."
    # X - U+274C
    # O - U+2B55

    sym_menu = create_choose_menu(tic.symbols)
    query.edit_message_text(text=msg, reply_markup=sym_menu)

    return GameState.START_TURN


def turn(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    user_choice = int(query.data) - 1
    moves[user_choice] = cur_sym

    if tic.check_winers(moves, cur_sym, user_choice):
        game_board = create_board(moves)
        query.edit_message_text(text="Вы выиграли!\nGame over!!!",
                                reply_markup=game_board)

        return ConversationHandler.END

    bot_choice = ai.get_bot_turn(moves, next_sym, bot_mode)
    moves[bot_choice] = next_sym

    if tic.check_winers(moves, next_sym, bot_choice):
        game_board = create_board(moves)
        query.edit_message_text(
            text="Вы проиграли(((\nGame over!!!",  reply_markup=game_board)

        return ConversationHandler.END

    if not tic.has_turns(moves):
        msg = "Ничья"
        game_board = create_board(moves)
        query.edit_message_text(
            text="Ничья, больше ходов нет.\nGame over!!!", reply_markup=game_board)

        return ConversationHandler.END

    msg = f"Ваш ход: {query.data}\nХод бота: {bot_choice + 1}"
    game_board = create_board(moves)

    query.edit_message_text(text=msg, reply_markup=game_board)

    return GameState.USER_TURN


def end_game(update: Update, context: CallbackContext):
    global moves
    moves = tic.init_board
    update.effective_chat.send_message("До новой игры!")

    return ConversationHandler.END


def select(update: Update, context: CallbackContext):
    global cur_sym
    global next_sym
    global moves

    query = update.callback_query
    query.answer()

    cur_sym = query.data
    next_sym = tic.symbols[1 - tic.symbols.index(cur_sym)]

    moves = tic.init_board()

    sym = tic.get_first_turn(tic.symbols)
    if sym == cur_sym:
        msg = f"Ваш выбор: {cur_sym}\n Начинаем, ваш ход..."
    else:
        bot_choice = ai.get_bot_turn(moves, next_sym, bot_mode)
        moves[bot_choice] = next_sym
        msg = f"Ваш выбор: {cur_sym}\nПервым начинают - {next_sym}.\nИ ход соперника - {bot_choice + 1}"

    game_board = create_board(moves)

    query.edit_message_text(text=msg, reply_markup=game_board)

    return GameState.USER_TURN
