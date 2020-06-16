# Fifth task

my_second_list = [9, 8, 3, 3, 2]
print('Рейтинг на данный момент:' + str(my_second_list))
x = int(input('Добавте число в рейтин:'))

'''Это была попытка просто обрабоать исключение, но что-то всё равно пошло не так)'''
# try:
#     x = int(input('Добавте число в рейтин:'))
# except ValueError as err:
#     print('Вы ввели не чило')

'''Это была попытка на проврку числа и повторных попыток, но она работала не исправно пытаюсь доработать'''
# while True:
#     x = input('Добавте число в рейтин:')
#     if x.isdigit():
#         pass
#     else:
#         print('Возможно вы вели не число попробуйте снова:)')
#     break

my_second_list.append(x)
print(sorted(my_second_list, reverse=True))