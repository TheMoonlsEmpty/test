import random
a = list()
b = list()
for i in range(10):
   a.append(random.randint(10, 20))
   b.append(random.randint(10, 20))
print(a)
print(b)
c = set()
d = set()
for i in a:
    c.add(i)
print("a组不同的数", c)

for j in b:
    d.add(j)
print("b组不同的数", d)
print("不同的数：", len(c.union(d)), c.union(d))
print("重复的数：", len(c.intersection(d)), c.intersection(d))
print("不重复的数", len(c.union(d)-c.intersection(d)), c.union(d)-c.intersection(d))







