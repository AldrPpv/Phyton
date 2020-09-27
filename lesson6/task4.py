class Car:
    speed = 0
    color, name = None, None
    is_police = None

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def direction(self, way):
        print("Машина повернула", way)

    def show_speed(self):
        print(f'Скорость равна: {self.speed}')

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class TownCar(Car):
    def show_speed(self):
        print("Скорость TownCar (км/ч):", self.speed)
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print("Скорость WorkCar (км/ч):", self.speed)
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    pass


tc = TownCar(70, "RED", "AUDI", False)
sc = SportCar(140, "GREEN", "FERRARI", False)
wc = WorkCar(30, "BLUE", "BMW", False)
pc = PoliceCar(60, "YELLOW", "JEEP", True)

tc.show_speed()
tc.direction("на право")
print(f"Её цвет {tc.color}, её марка {tc.name}\n")

sc.show_speed()
sc.direction("на лево")
print(f"Её цвет {sc.color}, её марка {sc.name}\n")

wc.show_speed()
wc.direction("на назад")
print(f"Её цвет {wc.color}, её марка {wc.name}\n")

pc.show_speed()
pc.direction("на право")
print(f"Её цвет {pc.color}, её марка {pc.name}\n")