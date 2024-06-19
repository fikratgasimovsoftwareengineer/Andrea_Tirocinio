
import math
class Shape:

    def __init__(self,color):
        self.color = color


class Rectangle(Shape):
    def __init__(self,color, base, altezza):
        super().__init__(color)
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimeter(self):
        return 2 * (self.base + self.altezza)

class Circle(Shape):
    def __init__(self,color, raggio):
        super().__init__(color)
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio**2

    def perimeter(self):
        return 2 * math.pi * self.raggio

class Triangle(Shape):
    def __init__(self,color, lato1,lato2,lato3):
        super().__init__(color)
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

# Sono stato obbligato a prendere questa formula un pò complicata per calcolare l'area
# perché si dovevano usare gli stessi dati per area e perimetro. Altrimenti b*h/2 ed era
# fatta

    def area(self):
        s = self.perimeter() / 2  # semiperimetro
        return math.sqrt(s * (s - self.lato1) * (s - self.lato2) * (s - self.lato3))
    
    def perimeter(self):
        
        return self.lato1 + self.lato2 + self.lato3
    
def main():

    # istanzio le figure con variabile e richiamo le classi

    rct = Rectangle("red",5,3)
    crl = Circle("blue",4)
    trg = Triangle("green",4,3,2)

    print(f"Rectangle: Color: {rct.color}, Area: {rct.area()}, Perimeter: {rct.perimeter()}")
    print(f"Circle: Color: {crl.color}, Area: {crl.area()}, Perimeter: {crl.perimeter()}")
    print(f"Triangle: Color: {trg.color}, Area: {trg.area()}, Perimeter: {trg.perimeter()}")

    
if __name__ == "__main__":
    main()
