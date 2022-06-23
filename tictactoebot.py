from telegram.ext import (Dispatcher, Updater, CommandHandler,
                          ConversationHandler, CallbackQueryHandler, MessageHandler)
import cmd_handlers as chdl
from const import GameState

digits = "|".join([str(i) for i in range(1, 10)])
digit_pattern = f"^{digits}$"

game_state_hdl = ConversationHandler(
    entry_points=[CommandHandler('new_game', chdl.new_game)],
    states={
        GameState.BOT_MODE: [CallbackQueryHandler(
            chdl.bot_mode)],
        GameState.START_TURN: [CallbackQueryHandler(
            chdl.select)],
        GameState.USER_TURN: [CallbackQueryHandler(
            chdl.turn, pattern=digit_pattern)],
    },
    fallbacks=[CommandHandler('end_game', chdl.end_game)]
)


def get_tocken() -> str:
    with open("env.txt") as ifile:
        data = ifile.read()
    return data.strip()


def init_handlers(dispather: Dispatcher):
    dispather.add_handler(CommandHandler(['start', 'help'], chdl.start))
    dispather.add_handler(game_state_hdl)


def run():
    bot_token = get_tocken()

    updater = Updater(
        token=bot_token, use_context=True)
    print("Tick tack toe bot starterd work...")

    dp = updater.dispatcher
    init_handlers(dp)

    updater.start_polling(poll_interval=1, drop_pending_updates=True)
    updater.idle()
