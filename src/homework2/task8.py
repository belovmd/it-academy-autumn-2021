"""Task
https://www.hackerrank.com/challenges/py-if-else/problem
Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format: A single line containing a positive integer, n.
Constraints: 1 <= n <= 100
Output Format: Print Weird if the number is weird. Otherwise, print Not Weird.
"""

n = 0
while n < 1 or n > 100:
    n = int(input("Введите число от 1 до 100: "))
    if 0 < n < 101:
        break
    else:
        print("Введённое число вне разрешённого диапазона! Введите число от 1 до 100")

if n % 2:
    print("Weird")
elif 1 < n < 6:
    print("Not Weird")
elif 5 < n < 21:
    print("Weird")
elif n > 20:
    print("Not Weird")


"""https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
   The provided code stub reads two integers from STDIN, a and b.
   Add code to print three lines where:
   The first line contains the sum of the two numbers.
   The second line contains the difference of the two numbers (first - second).
   The third line contains the product of the two numbers.
"""

a = int(input('Введите число а: '))
b = int(input('Введите число b: '))

print('The sum of two numbers:', a + b)
print('The difference of two numbers:', a - b)
print('The product of two numbers:', a * b)


"""https://www.hackerrank.com/challenges/python-loops/problem
   The provided code stub reads and integer, n, from STDIN.
   For all non-negative integers i < n, print i**2.
"""

n = int(input('Введите число n: '))

i = 0
while i < n:
    print(i ** 2)
    i += 1

print()


"""https://www.hackerrank.com/challenges/triangle-quest-2/problem
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you.
'for i in range(1,int(input())+1):'
You have to complete the code using exactly one print statement.
Constraints: 0 < N < 10
Output Format: Print the palindromic triangle of size as explained above.
"""

# При решении задачи использовано свойство числа, состоящего из единиц:
# при возведении в квадрат такого числа, мы получаем как раз нужный палиндром.
# Пример: 1 ** 2 = 1, 11 ** 2 = 121, 111 ** 2 = 12321 и т.д.

for i in range(1, int(input('N: ')) + 1):
    print((111111111 // (10 ** (9 - i))) ** 2)


"""https://www.hackerrank.com/challenges/python-quest-1/problem
You are given a positive integer N. Print a numerical triangle of height (N - 1) like the one below:
1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines. The first line (the for statement) is already written for you.
You have to complete the print statement.

Input Format: A single line containing integer, N.
Constraints: 1 <= N <= 9
Output Format: Print N - 1 lines as explained above.
"""

for i in range(1, int(input('N: '))):
    print((111111111//(10 ** (9-i))) * i)
