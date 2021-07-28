'''Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format
A single line containing a positive integer, n.
Constraints
1 <= n <= 100
Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
'''

print('Enter a positive integer')
n = int(input())
if (n % 2) or ((not n % 2) and (6 <= n <= 20)):
    print('Weird')
elif ((not n % 2) and (2 <= n <= 5) or (20 < n <= 100)):
    print('No weird')


'''The provided code stub reads and integer, n, from STDIN.
For all non-negative integers i < n, print i^2.
Example
n = 3
The list of non-negative integers that are less than n = 3 is [0, 1, 2].
Print the square of each number on a separate line.
0
1
4
Input Format
The first and only line contains the integer, n.
Constraints
1 <= n <= 20
Output Format
Print n lines, one corresponding to each i.
'''

print('Enter an integer')
n = int(input())
if (n >= 1) and (n <= 20):
    for i in range(0, n):
        print(i ** 2)


'''В системе координат на плоскости выделяют четверти:
I-й четветри соответствуют точки, имеющие обе (x и y) положительные координаты
II-ая четверть: x < 0, y > 0
III-ая четверть: x < 0, y < 0
IV-ая четверть: x > 0, y < 0
Напишите программу, которая по заданным X и Y (целые числа, которые вводятся пользователем),
определяет координатную четверть и выводит "I", "II", "III" или "IV".
'''

print('Введите координату x')
x = int(input())
print('Введите координату y')
y = int(input())
if (x > 0) and (y > 0):
    print('Точка с такими координатами находится в I четверти')
elif (x < 0) and (y > 0):
    print('Точка с такими координатами находится в II четверти')
elif (x < 0) and (y < 0):
    print('Точка с такими координатами находится в III четверти')
else:
    print('Точка с такими координатами находится в IV четверти')


'''Напишите программу, которая по введённому натуральному числу определит,
является ли год с данным номером високосным и выведет количество дней в нём (365 или 366).
Подсказка: в соответствии с григорианским календарем, год является високосным,
если его номер кратен 4, но не кратен 100, а также если он кратен 400.
'''

print('Введите год, о котором Вы хотите узнать високосный ли он')
year = int(input())
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print('Год високосный')
else:
    print('Год не високосный')
