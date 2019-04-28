# range() 函数可创建一个整数列表，一般用在 for 循环中。

# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

ran = range(5)
print(ran)

#输出结果 range(0, 5)

rang = list(range(5))
print(rang)

#输出结果 [0, 1, 2, 3, 4]


ranges = list(range(0,10,3))     #步长为3
print(ranges)

#输出结果 [0, 3, 6, 9]


rann = list(range(0, -10, -1))    #负数
print(rann)

#输出结果 [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
