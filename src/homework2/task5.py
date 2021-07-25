"""Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""
# F(n) = F(n-1)+F(n-2)

n = int(input('Введите число n: '))
template = "Число Фибоначчи = {Fib}"
if n < 0:
    print('Negative')
elif n <= 1:
    Fib_n = n
    print(template.format(Fib=Fib_n))
else:
    Fib_n_2 = 0
    Fib_n_1 = 1
    Fib_n = Fib_n_2 + Fib_n_1
    for i in range(0, n - 2):
        Fib_n_2 = Fib_n_1
        Fib_n_1 = Fib_n
        Fib_n = Fib_n_2 + Fib_n_1
    print(template.format(Fib=Fib_n))
