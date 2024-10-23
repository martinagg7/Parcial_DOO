
#clase base
class Shape:
    def area(self):
        pass

#Clase circulo
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius    
#Clase cuadrado    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
         return self.side * self.side

#clase calculadora area
class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total_area= 0
        for shape in self.shapes:
            total_area+= shape.area()  
        return total_area
