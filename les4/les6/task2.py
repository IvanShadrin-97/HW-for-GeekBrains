"""
Тут получилсоь так что когда читал задание подумал что все констатны нужно сделать не измениямыми,
и вот полуичлось что-то сранное. Потом поговрил с наставником и понял что надо пределать в сторону изменяемых констант
"""

# class Road:
#     __length = 20
#     __width = 5000
#
#     def asphalt_mass(self):
#         mass = 25
#         thickness = 5
#         result = (Road.__length * Road.__width * mass * thickness) / 1000
#         print(f'{Road.__length}м * {Road.__width}м * {mass}кг * {thickness} = {int(result)}т')
#
#
# a = Road
# a.asphalt_mass(None)

"""Попытка номер 2"""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, thickness):
        result = (self._length * self._width * 25 * int(thickness)) / 1000
        print(f'{self._length}м * {self._width}м * 25кг * {thickness} = {int(result)}т')


a = Road(20, 5000)
a.asphalt_mass(5)

print(1)
