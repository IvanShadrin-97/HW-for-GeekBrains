"""Ниже каждое задание отедально"""

# First task

my_tuple = (1, 2, 3, 'Hello', True, False, 1.231)
my_list = [1, 2, 3, 'Hello', my_tuple, 4.20]

for i in my_list:
    print(type(i))

# Second task

a = input('Input some-thing: ')
a = list(a)

for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]

print(a)

# Third task(list)

num = int(input('Ведите целым числом месяц от 1-ого до 12-ого и мы подзакжем к какому времени года он относится:'))

season_list = ['Зима', 'Весна', 'Лето', 'Осень']

while True:
    if num <= 2 or num == 12:
        print(season_list[0])
    elif 3 <= num <= 5:
        print(season_list[1])
    elif 6 <= num <= 8:
        print(season_list[2])
    elif 9 <= num <= 11:
        print(season_list[3])
    else:
        print('Ведите корректное число')
    break

# Third task(dict)

nums = int(input('Ведите целым числом месяц от 1-ого до 12-ого и мы подзакжем к какому времени года он относится:'))

season_dict = {'key': 'Зима', 'key1': 'Весна', 'key2': 'Лето', 'key3': 'Осень'}

'''Честно я знаю что копи паст это не есть хорошо, но время поджимало со времением попробую другой способ решения 
возможно даже до сдачи данного ДЗ'''

while True:
    if nums <= 2 or nums == 12:
        print(season_dict.get('key'))
    elif 3 <= nums <= 5:
        print(season_dict.get('key1'))
    elif 6 <= nums <= 8:
        print(season_dict.get('key2'))
    elif 9 <= nums <= 11:
        print(season_dict.get('key3'))
    else:
        print('Ведите корректное число')
    break

# Fourth task

words = str(input('Ведите любое предложение:'))

number_of_words = 0
for k in words.split(' '):
    number_of_words += 1
    print(str(number_of_words) + ':' + k[0:10])

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

# Sixth task

goods = [
    (1, {'название': 'Компьютер', 'цена': '90000', 'количество': '7', 'eд': 'шт.'}),
    (2, {'название': 'Монитор', 'цена': '20000', 'количество': '3', 'eд': 'шт.'}),
    (3, {'название': 'Мышь игровая', 'цена': '2000', 'количество': '12', 'eд': 'шт.'}),
    (4, {'название': 'Клавиатура', 'цена': '4000', 'количество': '33', 'eд': 'шт.'})
]

for key, values in goods:
    print('В нашем ассортименте есть:' + values.get('название') + ', По ценне:' + values.get(
        'цена') + ', Остаток на складе:' + values.get('количество') + 'шт')

# Почему когда в послднем параметре указываю values.get('ед') выскаиквает TypeError?

needs = input('Ведите наименование товара который вы хотеле бы преобрести:')
