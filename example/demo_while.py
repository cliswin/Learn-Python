
x = 1
while x <= 100:
    print(x)
    x += 1



name = ''
while not name.strip():
    name = input('Please enter your name: ')
print('Hello, {}!'.format(name))
