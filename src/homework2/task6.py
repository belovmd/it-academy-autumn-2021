# 6. Определите, является ли число палиндромом
# (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами
# (без конвертации числа в строку или что-нибудь еще)

digits = int(input("Please, input the number for checking: "))
a = int(digits)
reverse_order = 0
while digits != 0:
    last_digit = digits % 10
    reverse_order = reverse_order * 10 + last_digit
    digits = int(digits // 10)
if a == reverse_order:
    print("Yes, that's a palindrome")
else:
    print("No, it's not a palindrome")
