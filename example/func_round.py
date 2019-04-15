# 函数round()把浮点数四舍五入为最接近的整数值。
# 注意：在python2.7版本中是如上所说，但是在python3.5版本中并不是这样的。

var = round(1/2)
print(var)

var = round(2.0/5.0)
print(var)

# 2.7版本：第一个var=0，第二个var=1.0； 3.5版本：第一个var=0.5，第二个var=0
