import time


class TrafficLigth:
    _color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            time.sleep(7)
            print(self._color[0])
            time.sleep(2)
            print(self._color[1])
            time.sleep(10)
            print(self._color[2])


traffic_ligth = TrafficLigth()
traffic_ligth.running()

print(1)
