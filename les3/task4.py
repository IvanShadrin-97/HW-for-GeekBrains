def my_func(x: int, y: int):
    try:
        if y >= 0:
            return print('Вы ввели не отрицательное число')
        elif y < 0:
            return x ** y
    except TypeError as e:
        print(e)


firs_number = int(input('Ведите число которое вы хотите возвести в степень:'))
second_number = int(input('Ведите отрицательное число, степень:'))
print(my_func(firs_number, second_number))
