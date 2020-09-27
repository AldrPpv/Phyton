import time


class TrafficLight:
    __color = ""

    def running(self):
        self.__color = "RED"
        print(self.__color)
        time.sleep(7)
        self.__color = "YELLOW"
        print(self.__color)
        time.sleep(2)
        self.__color = "GREEN"
        print(self.__color)
        time.sleep(5)


tL = TrafficLight()
tL.running()
