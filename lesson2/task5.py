# Fifth task

# При написани обработчика ошибки пучарм подсвечивает х из-за чего когда первый раз писал обработку убрал в комент
my_list = [9, 8, 3, 3, 2]
print('Рейтинг на данный момент:' + str(my_list))
try:
    x = int(input('Добавте число в рейтин:'))
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)

my_list.append(x)
print(sorted(my_list, reverse=True))


# while True:
#     x = input('Добавте число в рейтин:')
#     if x.isdigit():
#         break
#     else:
#         print('Возможно вы вели не число попробуйте снова:)')


#Этот вариант появился из-за активного обсуждения в чате на счёт sorted и можно ли его использовать.

def sort_time(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True


my_second_list = [6, 5, 3, 7, 2, 3]
add_to_list = int(input('Ведите число:'))
my_second_list.insert(1, add_to_list)
sort_time(my_second_list)
print(my_second_list)

