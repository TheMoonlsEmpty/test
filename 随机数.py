import random
a = list()
for i in range(10):
    a.append(random.randint(1, 10))   # 随机十个数
print(a)
b = []
c = []
for i in a:
    if i not in b:
        if a.count(i) > 1:
            print(i, a.count(i))
            b.append(i)
        else:
            c.append(i)
print("重复的个数:", len(b), "个,", "分别是：", b)
print("不重复的个数:", len(c), "个,", "分别是：", c)
