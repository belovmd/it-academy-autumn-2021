"""Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме
последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.
В единственной строке входного файла INPUT.TXT записано одно целое число N (0 ≤ N < 10 ** 6).
В выходной файл OUTPUT.TXT нужно вывести «YES», если билет с номером N счастливый и «NO» в противном случае.
https://acmp.ru/index.asp?main=task&id_task=52"""
A = int(input('Введите шестизначное число: '))
left = 0
right = 0

for i in range(6):
    if i < 3:
        left += A // 10**i % 10
    else:
        right += A // 10**i % 10

if A > (10 ** 6) or A < (10 ** 5):
    print('Ошибка ввода')
elif left == right:
    print('YES')
else:
    print('NO')


"""Как и многие другие девочки, Маша любит разные гадания. Некоторое время назад Маша узнала
новый способ гадать на числах – для какого-нибудь интересующего ее натурального числа n надо
посчитать сумму всех чисел, на которые n делится без остатка.Маша не очень любит арифметику,
и попросила вас написать программу, которая автоматизирует процесс гадания.
В единственной строке входного файла INPUT.TXT записано натуральное число n (n ≤ 1000),
которое Маша была вынуждена сообщить.
В выходной файл OUTPUT.TXT выведите сумму всех натуральных делителей числа n.
https://acmp.ru/index.asp?main=task&id_task=23"""
N = int(input('Введите число: '))
summ = 0

for x in range(1, N + 1):
    if N % x == 0:
        summ = x + summ

print(summ)


"""Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.
В единственной строке входного файла INPUT.TXT записано единственное целое число N, не превышающее
по абсолютной величине 10 в 4 степени.
В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму
чисел, расположенных между 1 и N включительно.
https://acmp.ru/index.asp?main=task&id_task=2"""
G = int(input('Введите целое число: '))
s = 0

for _ in range(1, G + 1):
    s = _ + s

print(s)


"""Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель 
за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись 
исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе.
Во входном файле INPUT.TXT сначала записано число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующей строке через пробел располагается N целых чисел, разделенных пробелами. Каждое число – 
среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50.
В выходной файл OUTPUT.TXT требуется вывести одно число – длину самой продолжительной оттепели, то есть 
наибольшее количество последовательных дней, на протяжении которых среднесуточная температура превышала 0 градусов. 
Если температура в каждый из дней была неположительной, выведите 0.
https://acmp.ru/index.asp?main=task&id_task=264"""
days = int(input('Дней: '))
s_ = input('Температуры: ').split()
t = 0
k = 0

for y in range(days):
    if int(s_[y]) > 0:
        k += 1
    else:
        if t < k:
            t = k
            k = 0
        if t < k:
            t = k

print(t)

"""Задана последовательность, состоящая только из символов ‘>’, ‘<’ и ‘-‘. 
Требуется найти количество стрел, которые спрятаны в этой последовательности. 
Стрелы – это подстроки вида ‘>>-->’ и ‘<--<<’.
В первой строке входного файла INPUT.TXT записана строка, состоящая из 
символов ‘>’, ‘<’ и ‘-‘ (без пробелов). Строка состоит не более, чем из 250 символов.
В единственную строку выходного файла OUTPUT.TXT нужно вывести искомое количество стрелок.
https://acmp.ru/index.asp?main=task&id_task=44"""
str_ = '<<<<>>--><--<<--<<>>>--><<<<<'
strela = 0

for z in range(0, len(str_)):
    if str_[z:][:5] == '>>-->':
        strela += 1
    elif str_[z:][:5] == '<--<<':
        strela += 1

print(s)
