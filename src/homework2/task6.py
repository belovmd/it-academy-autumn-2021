''' Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
'''
n = int(input("write a number=>"))
a = n
b = 0
while(n > 0):
    last = n % 10
    b = b * 10 + last
    n = n // 10
if a == b:
    print("number palindrome")
else:
    print("number no palindrome")
