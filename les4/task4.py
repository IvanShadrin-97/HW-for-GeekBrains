from itertools import count
'''
Это задние понял после вашего 5-ого урока, не разобрался с функцией count во время самостоятельного решения.
'''
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_gen = [i for i in my_list if my_list.count(i) == 1]
print(my_gen)
