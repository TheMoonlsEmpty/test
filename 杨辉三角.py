# 方法一:

# s = [1]
# print(s)
# while len(s) < 7:
#     for i in range(1, len(s)):
#         s[i] = pre[i - 1] + pre[i]   # s[i]表示修该之前的值。
#     s.append(1)    # 末尾追加
#     pre = s.copy()
#     print(s)

# 方法二:

curl = [1]
print(curl)
for i in range(1, 7):
    for j in range(1, i):
        curl[j] = pre[j-1]+pre[j]
    curl.append(1)
    pre = curl.copy()
    print(pre)