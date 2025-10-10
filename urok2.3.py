x = input('Введи число x: ')
y = input('Введи число y: ')
expected = input('Введи ОР: ')
x = int(x)
y = int(y)
expected = int(expected)


result = y / 2 ** 3 + x
print(result == expected)