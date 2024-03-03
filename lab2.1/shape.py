from abc import ABC, abstractmethod
class Shape():
    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
        
    @abstractmethod
    def calculate_area(self):
        pass
