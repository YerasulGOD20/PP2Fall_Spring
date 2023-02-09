'''                     #1task
class Popsik():
    def __init__(self):
        self.str1 = ""
    def getString(self):
        self.str1 = input()
    def printString(self):
        print(self.str1.upper())
str1 = Popsik()
str1.getString()
str1.printString()
'''
'''
class shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class square(shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Fall = square(3)
print(Fall.area())    
print(square().area()) 
'''
'''
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def 
    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
'''
'''
import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
'''


