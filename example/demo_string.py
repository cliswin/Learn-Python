# center 字符串居中

str = 'hello python'.center(39,'*')
print(str)


# find  在字符串中查找子串，如果找到就返回字串的第一个字符的索引

title = 'Monty Python Flying Circus'.find('Python')
print(title)


# join  合并序列的元素 与split相反

dirs = '', 'usr', 'bin', 'env'
print('C:' + '\\'.join(dirs))

#  lower  返回字符串的小写版本

name = 'Gumby'
names = ['gumby', 'smitn', 'jones']
if name.lower() in names:
    print('Found it!')

# replace  将指定子串都替换成另一个字符串，并返回替换后的结果

rep = 'This is a test'.replace('is', 'eez')
print(rep)


# split  将字符串拆分成序列，如果没有指定分隔符，默认在单个或多个连续的空白字符处进行拆分

spl = '1+2+3+4+5'.split('+')
print(spl)

# strip 将字符串开头和末尾的空白，也可以是指定的开头和末尾的字符（但不包括中间的空白）删除，并返回删除后的结果

stri = '*** internal whitespace is kept!!! ***'.strip(' *!')
print(stri)