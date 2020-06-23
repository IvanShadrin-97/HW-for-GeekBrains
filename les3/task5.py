"""
Вот что было до просмотра 4 урока. Пока что не получается выстравиать очень большие цепочки логики,
старюсь как могу но в голову не приходит дальнешие действия.
"""
# def infity_sum(*args):
#     while True:
#         x = input('Видите числа через пробел')
#         x.split(' ')
#         args = sum(x)
#         break
#     print(args)

"""
Ваш код.
Для самостоятельной практики.
"""


def insert_sum(*args):
    result = 0
    exit_flag = False
    for itm in args:
        try:
            result += float(itm)
        except ValueError:
            if itm == 'q':
                exit_flag = not exit_flag
                break
        return result, exit_flag


user_sum = 0
user_exit = False
while not user_exit:
    user_input = input('Введитечисла черз прбел:').split(' ')
    result_summ, user_exit = insert_sum(*user_input)
    user_sum += result_summ
    print(f'сумма:{user_sum}')
