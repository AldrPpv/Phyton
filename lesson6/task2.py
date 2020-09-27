class Road:
    _length = 0.0
    _width = 0.0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_asphalt(self, _weight, thickness):
        return self._length * self._width * _weight * thickness


my_road = Road(20, 5000)
weight = my_road.weight_asphalt(25, 5)
print(weight)