# 设计一个斐波那契数列类，实现其实例可调用：

# 方法一:

class Fib:
    """0,1,1,2,3,5   ,8,13,21"""

    def __init__(self):
        self.lst = []

    def __call__(self, n, *args, **kwargs):
        i = 0
        prev, next = 0, 1
        while True:
            self.lst.append(prev)
            if i == n:
                return prev
            prev, next = next, prev + next
            i += 1

    def __getitem__(self, item):
        return self.__call__(item)


f1 = Fib()
# print(f1(7))
print(f1(21))
# print(f1[5])


# 方法二：(添加在列表,并显示出来)
class Feb:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.c = [1]
    def __call__(self, n, *args, **kwargs):
        for i in range(n-1):
            sum = self.a+self.b
            self.a = self.b
            self.b = sum
            self.c.append(sum)
        print(self.c)
        return self.c[n-1]
a=Feb()
print(a(12))

# 方法三：(没有添加到列表)

class Feb:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __call__(self, n,*args,**kwargs):
        for i in range(n):
           self.a, self.b = self.b, self.a+self.b
        return self.a
a=Feb()
print(a(15))
