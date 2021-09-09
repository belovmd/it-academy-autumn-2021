"""Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""
# F(n) = F(n-1)+F(n-2)

n = int(input('Введите число n: '))
template = "Число Фибоначчи = {fib}"
a = 0
b = 1
if n < 0:
    print('Negative')
elif n <= 1:
    b = n
    print(template.format(fib=b))
else:
    a, b = b, a + b
    for i in range(n - 2):
        a, b = b, a + b
    print(template.format(fib=b))
