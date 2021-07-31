"""4. Посчитать количество строчных (маленьких) и прописных (больших) букв
   в введенной строке. Учитывать только английские буквы.
"""

print('Посчитаем количество строчных (маленьких) и прописных (больших) букв')
print('Введите строку для анализа: ')
s = str(input())

k_propisn = 0
k_strochn = 0
Propis = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Stroch = 'abcdefghijklmnopqrstuvwxyz'

print('Подсчёт количества букв в строке - ', s)

for i in range(0, len(s)):
    for j in range(0, 26):
        if s[i] == Propis[j]:
            k_propisn = k_propisn + 1
            break
        elif s[i] == Stroch[j]:
            k_strochn = k_strochn + 1
            break
print()
print('Во введённой строке найдено букв:')
print('Прописных:', k_propisn)
print('Строчных:', k_strochn)
