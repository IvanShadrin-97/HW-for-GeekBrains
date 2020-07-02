class Stationery:
    def __init__(self):
        self.title = 'This is title'

    def draw(self=None):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self=None):
        print('Рисуем ручкой')


class Pencil(Stationery):

    def draw(self=None):
        print('Рисум карандашом')


class Handle(Stationery):

    def draw(self=None):
        print('Рисуем маркером')


Stationery.draw()
Pen.draw()
Pencil.draw()
Handle.draw()
"""
Так и не понял почему от меня требуется это значение в поле draw...
Начал смотреть 7ой урок и пришёл к решению передать в селф None сразу
"""
print(1)
