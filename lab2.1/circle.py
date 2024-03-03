from shape import Shape

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__("Circle", color)
        self._radius = radius

    def calculate_area(self):
        return 3.14 * self._radius ** 2
