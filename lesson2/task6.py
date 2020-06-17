goods = []

while True:
    name = input('Ведите название товара:')
    price = input('Укажите цену товара:')
    pieces = input('Сколько позиций осталось на складе:')
    measure = input('Укажите меру измерений(шт,м,м.куб, и т.д:)')
    finish = int(input('Если вы хотите завершить програму ведите 1:'))
    dictionery = {'название': name, 'цена': price, ' отсаток': pieces, 'ед': measure}
    if finish == 1:
        break
    else:
        for q in enumerate(goods):
            print(q)



