'''You are given a string and you have to find its first word.
The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.'''

s = input("write text:")
print(s.split()[:1])


'''Мне предоставили строку,
состоящую из русских букв разных регистров, и попросили очистить ее от заглавных букв.'''

letters = 'пуИКцурРУРВЦр'
clean_string = ''
for letter in letters:
    if not letter.isupper():
        clean_string += letter
letters = clean_string
print(letters)


'''Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... n.
Количество элементов (n) вводится с клавиатуры. Вывести на экран каждый член ряда '''

n = int(input(""))
a = 1
c = 0
for i in range(0, n):
    c = c + a
    a /= -2
    print(a)


'''Дан список lst = [83, 2, 8, 32, 1, 3, 20, 132, 42, 4, 567, 3, 20].
  Необходимо вывести элементы, которые одновременно
  1) меньше 30
  2) делятся на 3 без остатка.
  Все остальные элементы списка необходимо просуммировать и вывести  результат.'''

med = 30
dn = 3
lst = [83, 2, 8, 32, 1, 3, 20, 132, 42, 4, 567, 3, 20]
smt = 0
for i in lst:
    if (i < med) and (i % dn == 0):
        print(i)
    else:
        smt += i
print('suma: ', smt)


'''Дан список из целых чисел. 
   Для каждого входящего в список числа вывестисколько раз оно встречается в списке.
   Если число встречается в списке несколько раз, то вывести его только один раз.
   Также вывести количество различных чисел в списке.'''

a = [8, 5, 4, 5, 5, 5, 4, 9, 2, 9, 2, 3, 0]
cnt = 0
for i in range(len(a)):
    for j in range(i):
        if a[i] == a[j]:
            break
    else:
        cnt += 1
        print('Число', a[i], ', количество:', end=' ')
        n = 1
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                n += 1
        print(n)
print('Различных чисел:', cnt)
