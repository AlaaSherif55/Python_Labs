from shape import Shape

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__("Rectangle", color)
        self._length = length
        self._width = width
    
    def calculate_area(self):
        return self._length * self._width