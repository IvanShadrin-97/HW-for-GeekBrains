"""
Данную задчу решал уже после просмотра 7-ого урока, так что возможно это будет ваш код для практики,
но попробую рещить другим способом=)
"""


class Car:
    """
    После того как задал флоат=0 по умолчанию в методе колор и нейм стали подсвечиваться красным,
    я посмотрел в ваш код и вас стоит speed в конце перд полис можете объяснить почему так происходит?
    """
    def __init__(self, speed: float = 0, color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is go')

    def stop(self):
        print('Car stopped')

    def turn(self, side):
        # if side is 'Left' or 'Right':  Сдесь изначльно было вот так
        if side in ('Left', 'Right'):
            print(f'Car turn {side}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Your speed out of range')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Your speed out of range')


"""
В этом задние ничего не сказано про изменения метода полис кара,
так что оставлю для практики просто препишу и закоментирую=)
"""


class Police_Car(Car):
    pass

    # def __init__(self, color, name, is_sherif):
    #     self.is_sherif = is_sherif
    #     super().__init__(float('inf'), color, name , True)
