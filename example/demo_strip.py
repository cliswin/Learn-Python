# strip 将字符串开头和末尾的空白，也可以是指定的开头和末尾的字符（但不包括中间的空白）删除，并返回删除后的结果

stri = '*** internal whitespace is kept!!! ***'.strip(' *!')
print(stri)

#输出结果：internal whitespace is kept
