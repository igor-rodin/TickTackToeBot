# для тестирования AI
# для понимания, как AI встраивать в телегобота

import data_module as dm
import botai

dm.init()  # начальное заполнение поля битвы

game_result = 'None'  # результат игры


# настройка игры - это надо как то встроить в бота - изначальный выбор параметров
x_turn = True  # Х - ходят первые
bot_play_X = False  # Бот играет за O
bot_algorithm = 3  # Алгоритм игры бота
# 1 - тупо выбирает первую свободную ячейку
# 2 - случайно выбирает одну из свободных ячеек
# 3 - считает все поле, не может проиграть

while game_result == 'None':
    dm.PrintField(dm.field)  # красиво рисуем поле битвы
    if x_turn:
        print('Ходят X')
        if bot_play_X:
            dm.field = dm.field.replace(botAI.get_bot_turn(
                dm.field, 'X', bot_algorithm), 'X')  # бот сходил за X
        else:
            dm.field = dm.field.replace(
                dm.MyInput(dm.field), 'X')  # чел сходил за X
    else:
        print('Ходят O')
        if not bot_play_X:
            dm.field = dm.field.replace(botAI.get_bot_turn(
                dm.field, 'O', bot_algorithm), 'O')  # бот сходил за O
        else:
            dm.field = dm.field.replace(
                dm.MyInput(dm.field), 'O')  # чел сходил за O
    # проверяем, чего там с результатом игры
    game_result = dm.CheckGame(dm.field)
    x_turn = not x_turn

print('Игра окончена')
dm.PrintField(dm.field)
print(game_result)
