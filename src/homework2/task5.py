'''Выведите n-ое число Фибоначчи,
используя только временные переменные,
 циклические операторы и условные операторы. n - вводится'''
n = int(input("введите ряд"))
f1 = f2 = 1
for i in range(2, n):
    f1,f2 = f2,f1+f2
print(f"Число Фибоначчи для ряда {n} равно {f2}")