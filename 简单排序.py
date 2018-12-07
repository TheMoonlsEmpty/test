import random
a = list()
for i in range(10):
    b = random.randint(1, 20)
    a.append(b)
print(a)
for j in range(9):
    for k in range(0, 9-j):
        if a[k] < a[k+1]:
           a[k], a[k+1] = a[k+1], a[k]
print(a)

