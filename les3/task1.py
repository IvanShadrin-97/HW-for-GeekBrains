def dvision(x: int, y: int) -> int:
    try:
        result = x / y
        return result
    except ZeroDivisionError as e:
        print(e)


x = int(input('Ведите первое число:'))
y = int(input('Ведите второе число:'))

print(dvision(x, y))