# 方法一:
m = int(input("输入一个数字m="))    # 指定行数
k = int(input("输入一个数字k="))    # 指定行数的第几位数
curl = [1]
for i in range(1, m):
    for j in range(1, i):
        curl[j] = pre[j-1]+pre[j]
    curl.append(1)
    pre = curl.copy()
print(pre)
print(pre[k-1])

# 不成熟版:

# m = int(input("输入一个数字m="))
# k = int(input("输入一个数字k="))
# for i in range(1, m):
#     a = 1
#     for x in range(1, i + 1):
#         a = x*a
#         if x+1 == k:
#             b = a
#         if x == m-k:
#             c = a
# print(a)
# print(b)
# print(c)
# print(a//(b*c))
# 第n行第m个为：（n-1）!/((m-1)!*(n-m)!)'