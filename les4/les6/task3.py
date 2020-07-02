"""
Эту задчу не смог решить, вот что было до урока
"""

# class Worker:
#     wage_bonus = {'Wage': 50000, 'bonus': 5000}
#
#     def __init__(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._incom = Worker.wage_bonus
#
# class Position(Worker):
#
#     def get_name_incom(self):
#         super().__init__()
#         print(self.name, self.surname)

"""
Ваш код, для собственной практики, немного изменил что-бы сотвестовать условиям задчи) 
там get_full_name и get_total_income должны быть в Position если я правильно понял.+ добавил TypeHints
"""


class Worker:
    def __init__(self, position: str, name: str, surname: str, salary: int, bonus: int):
        self.position = position
        self.name = name
        self.surname = surname
        self._income = {'Wage': salary, 'Bonus': bonus}


"""
В этой закоментированной части кода я так и не смог добраться до инита в врокере я не уверен что логика правильнная,
но даже добраться до самого инита не получилось хз, подскажите как это сделать сейчас буду пробовать создать новый инит
и после сделать две функции.
"""


# class Position(Worker):
#     def get_full_name(self):
#         return super().__init__(f'{self.name} {self.surname}')
#
#     def get_full_income(self):
#         super(Worker, self).__init__(salary, bonus)
#         return sum(self._income.values())
"""
Тут я сделал всё что в моих сиалх на данный момент в моей голове, но ничего не заработало
"""
class Position(Worker):
    def __init__(self, position_name: str, name: str, surname: str, salary: int, bonus: int):
        self.position_name = position_name
        super(Worker, self).__init__(name, surname, salary, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    a = Worker('Менеджер', 'Vasya', 'Pupkin', 50000, 2500)
    b = Position
    b.get_full_income()
    b.get_full_name()
    print(1)


