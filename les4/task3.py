# Сделал  доп переменую для читаемости
my_gen = ([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])
print(my_gen)

# В одну строку
print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])
