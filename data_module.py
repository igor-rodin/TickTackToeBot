# Тут храним массив, который карта поля и нужные функции для обработки этого массива

field:str = '' # Да, данные будут в строке

win_patterns = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) # если в этих позициях
                                                                                     # стоят XXX или OOO,
                                                                                 # то кто-то выйграл

def init(): # изначально заполняем масиив
    global field
    field = '123456789'

##### ДЛЯ ОТЛАДКИ, В ПРОДАКШИН НА БОТА - ФУНКЦЯ НЕ НУЖНА #####
def PrintField(local_field): # функция печати состояния игрового поля 
    print('-' * 13)
    for i in range(3): # печатаем целыми строками
        print(f'| {local_field[i*3]} | {local_field[i*3 + 1]} | {local_field[i*3 + 2]} |')
        print('-' * 13)
############################################


##### ДЛЯ ОТЛАДКИ, В ПРОДАКШИН НА БОТА - ФУНКЦЯ НЕ НУЖНА #####
def MyInput(local_field): # функция ввода человеком нового элемента (с проверками)
    num = int(input('Введите позию, куда хотите сходить 1..9: ')) # проверку на нецифру делать не стал
    while True:
        if not ((0 < num) and (num < 10)):
            print('Ввели неправильное место на поле')
        elif not(local_field[num-1] in '123456789'): # если поле занято, то вместо цифры там X или O
            print('Это поле уже занято')
        else: return str(num)
        num = int(input('Введите позицию, куда хотите сходить 1..9: '))
############################################


def CheckGame(local_field): # функция проверки окончания игры - сразу возвращает результат игры
    if len(local_field.replace('X','').replace('O','')) == 0: return 'Победила дружба! Ничья!'
    if 'XXX' in list(filter(lambda x: x,[local_field[win_patterns[i][0]]+\
                                         local_field[win_patterns[i][1]]+\
                                         local_field[win_patterns[i][2]] \
                                    for i in range(len(win_patterns))])):
        return 'XXX Победили крестики XXX'
    if 'OOO' in list(filter(lambda x: x,[local_field[win_patterns[i][0]]+\
                                         local_field[win_patterns[i][1]]+\
                                         local_field[win_patterns[i][2]] \
                                    for i in range(len(win_patterns))])):
        return 'OOO Победили нулики OOO'
    return 'None' # результата игры еще нет - можно продолжать играть
