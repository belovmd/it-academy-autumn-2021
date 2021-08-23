""" Задача уровня  elementary c сайта https://py.checkio.org.
You are given a string and you have to find its first word.
"""
str_ = "Hello World"
word = str_.split()  # делим строку на слова
print(word[0])       # выводим первое слово

""" Задача уровня  elementary c сайта https://py.checkio.org.
you need to create a password verification function.
The verification condition is:
the length should be bigger than 6
"""
parol = input(" Введите пароль: ")
if len(parol) > 6:
    print("Подходящий пороль")
else:
    print("Введите больше символов")

""" Задача уровня  elementary c сайта https://py.checkio.org.
You have a positive integer. Try to find out how many digits it has?
"""
chislo = int(input())
chislo1 = str(chislo)
print("Колличество цифр числа", chislo, '-', len(chislo1))

""" Задача easy с сайта  www.hackerrank.com. Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird"""
n = int(input().strip())
if n % 2 != 0:
    print('Weird')
if 2 <= n <= 5:
    print('Not Weird')
if 6 <= n <= 20:
    print('Weird')
if n > 20:
    print('Not Weird')
