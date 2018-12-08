# 设计 二维坐标 Point 类，使其可hash，并能判断2个坐标实例是否相等，实现2个坐标加减运算，以及判断2个坐标实例的大小
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{},{}'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __iadd__(self, other):
        return Point((self.x + other.x), (self.y + other.y))


p1 = Point(7, 5)
p2 = Point(3, 5)

print(p1 == p2)
p1 += p2
print(p1)






