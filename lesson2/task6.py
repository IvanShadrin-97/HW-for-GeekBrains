"""Вот что было до.Так и не смог дойти понять какой алгоритм использовать дальше"""

# goods = []
#
# while True:
#     name = input('Ведите название товара:')
#     price = input('Укажите цену товара:')
#     pieces = input('Сколько позиций осталось на складе:')
#     measure = input('Укажите меру измерений(шт,м,м.куб, и т.д:)')
#     finish = int(input('Если вы хотите завершить програму ведите 1:'))
#     dictionery = {'название': name, 'цена': price, ' отсаток': pieces, 'ед': measure}
#     if finish == 1:
#         break

'''Ниже Ваш код.
Это было сделанно исключительно для себя что-бы во время написания кода думать над его струтурой 
и синтаксисом использованном в нём.'''

products_template = {
    'название': ('Название товара', str),
    'цена': ('Стоймость товара', int),
    'колчиество': ('Количество позиций на складе', int),
    'измерение': ('Единицы измерения (шт, кг, м,и т.д...)', str)
}

next_enter = True

auto_inc = 1
products_list = []

while next_enter:
    product = {}
    for key, value in products_template.items():
        while True:
            user_values = input(f'{value[0]}\n')
            try:
                user_values = value[1](user_values)
            except ValueError:
                print(f'Вы велли не вернное занчение.')
                continue
            product[key] = user_values
            break
    products_list.append((auto_inc, product))
    auto_inc += 1

    while True:
        next_add = input('Добавть ещё продукт? Да/Нет \n')
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'Да'
            break
        else:
            print('Неперный ввод, повторите попытку')

print(products_list)

product_analitics = {}

for key in products_template:
    result = []
    for itm in products_list:
        result.append(itm[1][key])
    product_analitics[key] = result

print(product_analitics)








