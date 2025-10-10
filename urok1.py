 text1 = 'life'
text2 = 'is'
text3 = 'beautiful'

print(text1 + ' ' + text2 + ' ' + text3)


a=5
b=7

print(a + b)
result_a_b = a + b
print(result_a_b)


k = 42
l = 57
m = 83
n = 14
# x * 2 ** 3 / 2 + y
print(k * 2 ** 3 / 2 + l)
print(l * 2 ** 3 / 2 + m)
print(m * 2 ** 3 / 2 + n)
print(n * 2 ** 3 / 2 + k)


def calculate (x, y):
    print(x * 2 ** 3 / 2 + y)

calculate(k, l)
calculate(l, m)
calculate(m, n)
calculate(n, k)

def calculate_2(x, y):
    result = x * 2 ** 3 / 2 + y
    return result

result_k_l = calculate_2(k, l)
print(result_k_l)
print(calculate_2(k, l))


def work():
    print('I am working')

work()


o = 8
if o < 5:
    print('Привет')
else:
    print('Пока')



o = 4
if o < 5:
    print('Привет')
elif o >= 5 and o < 10:
    print("Привет, привет")
else:
    print('Пока')