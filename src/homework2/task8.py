"""
Task_8_1 https://www.hackerrank.com/challenges/capitalize/problem
Difficulty - Easy
You are asked to ensure that the first and last names of people begin with
a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.
Input Format:
A single line of input containing the full name, S.
Constraints:
* 0<len(S)<1000
* The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when
capitalized remains 12abc.
Output Format:
Print the capitalized string, S.
"""
my_str_ = input('Input the string: ')
while len(my_str_) > 1000 or not len(my_str_):
    print('Incorrect value')
    my_str_ = input('Please, input the string: ')
if my_str_.istitle():
    print('The capitalized string is :', my_str_)
else:
    clear_str_ = my_str_.split(' ')
    template = "The capitalized string is : \n{new_line}"
    new_line = ''
    for word in clear_str_:
        if word[0].isdigit():
            new_line += word + ' '
        else:
            new_line += word[0].upper() + word[1:len(word)] + ' '
    print(template.format(new_line=new_line))

"""
Task_8_2 https://www.hackerrank.com/challenges/python-print/problem
Difficulty - Easy
The included code stub will read an integer,n, from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
Example:
n=5
Print the string 12345.
Input Format:
The first line contains an integer n.
Constraints:
1<=n<=150
Output Format:
Print the list of integers from 1 through n as a string, without spaces.
"""
n = int(input('Input n from 1 to 150: '))
if n < 1 or n > 150:
    print('Incorrect value')
    n = int(input('Input n from 1 to 150: '))
output_list = ''
for num in range(1, n + 1):
    output_list = output_list + str(num)
print(output_list)

"""
Task_8_3 https://www.hackerrank.com/contests/it-academy-02/challenges/challenge-1975/submissions
Difficulty: Medium
Напишите программу, которая по введённому натуральному числу определит,
является ли год с данным номером високосным и выведет количество дней в нём (365 или 366).
Подсказка: в соответствии с григорианским календарем, год является високосным,
если его номер кратен 4, но не кратен 100, а также если он кратен 400.
Input Format:
Одно натуральное число
Constraints:
1 сек
Output Format:
Одно натуральное число
Sample Input 0
2016
Sample Output 0
366
"""
day = int(input('Input the year: '))
if not day % 400:
    print('366')
elif not day % 4 and day % 100:
    print('366')
else:
    print('365')


"""
Task_8_4 https://www.hackerrank.com/challenges/triangle-quest-2/problem
Difficulty - Medium
You are given a positive integer.
Your task is to print a palindromic triangle of size.
For example, a palindromic triangle of size  is:
1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.
Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.
Input Format:
A single line of input containing the integer n.
Constraints:
0<n<10
Output Format:
Print the palindromic triangle of size n as explained above.

Sample Input
5
Sample Output
1
121
12321
1234321
123454321
"""
n = int(input('Input the number from 1 to 9: '))
while n < 1 or n > 9:
    print('Incorrect value')
    n = int(input('Input the number from 1 to 9: '))
for number in range(1, n + 1):
    for digit in range(1, number + 1):
        print(digit, end='')
    for reverse_num in range(number - 1, 0, -1):
        print(reverse_num, end='')
    print()

# после долгих изучений свойств функции print, найдено решение из 2-х строк (по условию задачи)
# тест на сайте не прошел, хотя условия соблюдены и код работает
#for num in range(1, int(input()) + 1):
#    print(*[dig for dig in range(1, num + 1)], *[dig for dig in range(num - 1, 0, -1)], sep='')


"""
Task_8_5 https://www.hackerrank.com/contests/it-academy-02/challenges/challenge-1978/problem
Difficulty - Medium
В системе координат на плоскости выделяют четверти:
I-й четветри соответствуют точки, имеющие обе (x и y) положительные координаты
II-ая четверть: x < 0, y > 0
III-ая четверть: x < 0, y < 0
IV-ая четверть: x > 0, y < 0
Напишите программу, которая по заданным X и Y (целые числа, которые вводятся пользователем),
определяет координатную четверть и выводит "I", "II", "III" или "IV"

Input Format:
Два целых числа
Constraints:
1 сек
Output Format:
Строка
Sample Input 0:
1
1
Sample Output 0:
I
"""
x = int(input('Input the X coordinate: '))
y = int(input('Input the Y coordinate: '))
if x > 0:
    if y > 0:
        print('I')
    else:
        print('IV')
else:
    if y > 0:
        print('II')
    else:
        print('III')
