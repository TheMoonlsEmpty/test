sum = 0
for i in range(1, 6):
    a = 1
    for j in range(1, i+1):
        a = j*a
    sum = sum+a
print(sum)