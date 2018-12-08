a = [0, 1, 2, 3, 2, 1, 0]
b = [' ' * (3-i) + '*' * (2*i+1) for i in a]
for line in b:
  print(line)