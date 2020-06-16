# Fifth task

my_second_list = [9, 8, 3, 3, 2]
print('Рейтинг на данный момент:' + str(my_second_list))
x = int(input('Добавте число в рейтин:'))
my_second_list.append(x)
print(sorted(my_second_list, reverse=True))

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


#Этот вариант появился из-за активного обсуждения в чате на счёт sorted и можно ли его использовать.

def sorted(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True

my_list = [6, 5, 3, 2, 3]
add_to_list = int(input('Ведите число:'))
my_list.insert(1, add_to_list)
sorted(my_list)
print(my_list)

