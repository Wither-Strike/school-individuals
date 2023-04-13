import math
class rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __str__(self):
        return f"this is a rectangle with a length of {self.length}, a width of {self.width}, an area of {self.area()}, a perimeter of {self.perimeter()}, and a diagonal length of {self.diagonal()}"
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
    def diagonal(self):
        diagonalsquared = (self.length ** 2) + (self.width ** 2)
        return round((math.sqrt(diagonalsquared)), 2)

myrec = rectangle(5, 4)
print(myrec)