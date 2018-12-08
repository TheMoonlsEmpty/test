# 设计一个随机整数生成类，可以指定数值的范围，并且可以调整数字生成的个数

import random
class Randomint:  # 对象
    def __init__(self, count=10, start=1, stop=100):
        self.count = count
        self.start = start
        self.stop = stop
    def genint(self):
        s = []
        for i in range(self.count):

# 方法一:

#             s.append(random.randint(self.start, self.stop))   # 方法一
#         print(s)
# z = Randomint(10, 2, 100)
# z.genint()

#  方法二:（传参数方式不一样）

            return [random.randint(self.start, self.stop) for _ in range(self.count)]
list_a = Randomint(5, 20, 100)   # 可以传参控制输出个数和范围
list_a.genint()
print(list_a.genint())






# import random
# class RandomInt2:  # 工具类
#     @classmethod
#     def genint(cls, count=10, start=1, stop=100):
#         return [random.randint(start, stop) for _ in range(count)]
#
# RandomInt2.genint()  # 可以传参控制输出个数和范围






