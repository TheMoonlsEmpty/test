# 设计一个基类Shape,要求所有子类必须面积的计算，子类有：三角形，圆形，正方形
import math

class Shape:
    def __init__(self, n):
        self.n = n
    def area(self):
        raise type - error

class Triangle(Shape):
    def __init__(self, n, height):
        Shape.__init__(self, n)
        self.height = height

    def area(self):
        area = self.n*self.height/2
        print(area)

class Circular(Shape):
    def area(self):
        area = math.pi*self.n**2
        print(area)

class Square(Shape):
    def area(self):
        area = self.n**2
        print(area)

a = Triangle(5, 3)    # 实列化三角形
a.area()              # 三角形的面积

b = Circular(2)       # 实列化圆
b.area()              # 圆的面积

c = Square(3)         # 实列化正方形
c.area()              # 正方形的面积


