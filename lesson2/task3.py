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
