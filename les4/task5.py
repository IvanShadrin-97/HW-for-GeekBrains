from functools import reduce

"""
Возможно немного не правильно понял задние когда с наставником обсуждал данное здание 
там получилось немного другое решение, ествтвенно и ответ получается другой.
Тут тоже можно использовать лямбду, но когда писал код решние получилось таким.
"""


def my_func(prev_el, el):
    return prev_el + el


my_gen = ([i * i for i in range(100, 1001) if i & 1 == 0])
print(reduce(my_func, my_gen))
# print(reduce(lambda x, y: x + y, my_gen))

"""
Вот такое
"""

my_gen_2 = ([i for i in range(100, 1001) if i & 1 == 0])
print(reduce(lambda x, y: x * y, my_gen_2))
