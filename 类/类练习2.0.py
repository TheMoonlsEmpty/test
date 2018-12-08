# 利用上题的类，生成20个随机数字，两两配对，形成二维坐标，并这些坐标打印出来
import random

# 方法一:

class Randomint7:
    def __init__(self, count=10, start=1, stop=100):
        self._count = count
        self.start = start
        self.stop = stop
        self._gen = self._generate()  # 生成器对象

    def _generate(self):
        # 用生成器的无限生成，要多少不在这里控制。
        while True:
            yield [random.randint(self.start, self.stop) for _ in range(self._count)]

    def generate(self, count=0):  # 这里做控制判断
        if count > 0:
            self._count = count
        #         return next(self._gen)
        ret = next(self._gen)
        return ret


ri = Randomint7()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '<Point {} : {}>'.format(self.x, self.y)


# ===================================================================#
# 两种变现形式:
# points = [Point(k, v) for k, v in zip(ri.generate(), ri.generate())]
points = [Point(*v) for v in zip(ri.generate(), ri.generate())]
# ===================================================================#
# 下面是三种显示方式：

print('第一种方法', points, len(points))
# =========================
for x in points:
    print('第二种方法', x)
# =========================
for point in points:
    print('第三种方法：<Point {} : {}>'.format(point.x, point.y))


# 方法二:

import random
class Sj:
    def __init__(self, count, start, end):
        self.count = count
        self.start = start
        self.end = end
    def show(self):
        list = [random.randint(self.start, self.end) for i in range(self.count)]
        print(list)
        print([(list[i], list[i+1])for i in range(0, self.count-1, 2)])
x = Sj(20,2,100)
x.show()