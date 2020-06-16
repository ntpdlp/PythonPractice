from abc import ABC, abstractmethod

#ABC = Abstract Base Class
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 2 * 3.14 * self.radius    


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side

# g = GraphicShape()
#print(g.calcArea()) # Error: Can't instantiate abstract class GraphicShape

c = Circle(10)
print(f"{c.calcArea():.2f}")

s = Square(10)
print(s.calcArea())

