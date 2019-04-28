# 打印数字1~100

# for number in range(1,101):
#     print(number)


# 小于100的最大平方值
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Did't find it! ")
