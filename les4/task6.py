"""Не заню правильно ли решил данную задачу ну вроде генерирует целые числа начания с укозаного поставил стоп на 1000"""
from sys import argv
from itertools import count, cycle

# _, from_number, *args = argv
#
# from_number = [i for i in range(int(from_number), 1001)]
# print(from_number)

x = int(input('Введите число с которого надо начать генерацию:'))
for i in count(x):
    if i >= 1000:
        break
    else:
        print(i)

y = 0
my_list = [10, 'Dasd', 323, 123.2312, 'aaaaa']
for i in cycle(my_list):
    if y > 10:
        break
    print(i)
    y += 1
