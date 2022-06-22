# Мозги для бота
from random import randint
import data_module as dm


# щаг бота - в зависимости от алгоритма
def get_bot_turn(local_field: str, my_char, algorithm):
    if algorithm == 2:
        return my_random(local_field)          # случайный
    elif algorithm == 3:
        return mega_brain(local_field, my_char)  # самый умный
    else:
        return first_free(local_field)         # самый тупой


def first_free(local_field: str):  # самый тупой - выбирает первое непустое поле
    return local_field.replace('X', '').replace('O', '')[0]


def my_random(local_field: str):  # случайно выбраем незанятое поле
    local_field = local_field.replace('X', '').replace('O', '')
    return local_field[randint(0, len(local_field)-1)]

# для mega_brain


def win_triple(triple: str, my_char):  # triple - строка из 3-х символов (цифры и Х и О)
    s = triple.replace(my_char, '')  # чистим X или O - что на вход дали
    if len(s) == 1 and s.isdigit():
        return s  # если одно место с числом осталось - то это то, что нам нужно
    return ''


# поверка, можем ли мы победить одним ходом, когда играем за my_char
def i_can_win(local_field, my_char):
    triples = [local_field[dm.win_patterns[i][0]] +
               local_field[dm.win_patterns[i][1]] +
               local_field[dm.win_patterns[i][2]]
               for i in range(len(dm.win_patterns))]  # список заполненных верт, гориз и диагоналей
    k = ''
    for i in range(len(triples)):  # проверка тройки символов на то, что одного из ни нехватает
        # для полного заполнения
        k = win_triple(triples[i], my_char)
        if k:
            break
    return k


def mega_brain(local_field: str, my_char):
    # проверяем, можем ли победить одним ходом
    ret = i_can_win(local_field, my_char)
    if ret:
        return ret  # можем!

    if my_char == 'X':
        alien_char = 'O'
    else:
        alien_char = 'X'

    # проверяем, может ли враг победить одним ходом
    ret = i_can_win(local_field, alien_char)
    if ret:
        return ret  # может! - ходим туда - ему назло!

    best_move = ['5', '1', '3', '7', '9', '2',
                 '4', '6', '8']  # лучшие ходы на поле

    # выбираем из лучших ходов, которые не заняты
    return [i for i in best_move if i in local_field.replace('X', '').replace('O', '')][0]
