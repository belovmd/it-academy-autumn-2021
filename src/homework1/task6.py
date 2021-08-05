'''6. Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
'''
digits = int(input("Please, input the number for checking: "))
a = int(digits)
reverse = 0
while digits != 0:
    last_digit = digits % 10
    reverse = reverse * 10 + last_digit  # mirroring the input number
    digits = int(digits / 10)
if a == reverse:
    print("Yes, that's a palindrome")
else:
    print("No, it's not a palindrome")
