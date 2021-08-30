# Даны два натуральных числа. Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

m = int(input())
n = int(input())
if m == n:
    print("These are equal")
else:
    while m != n:
        if m > n:
            m = m - n
        elif n > m:
            n = n - m
    else:
        print('The biggest common divisor: ', m)
