"""4. Посчитать количество строчных (маленьких) и прописных (больших) букв
   в введенной строке. Учитывать только английские буквы.
"""

print('Посчитаем количество строчных (маленьких) и прописных (больших) букв')
print('Введите строку для анализа: ')
s = str(input())

sum_big = 0
sum_small = 0
Big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Small_letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(0, len(s)):
    for j in range(0, 26):
        if s[i] == Big_letters[j]:
            sum_big = sum_big + 1
            break
        elif s[i] == Small_letters[j]:
            sum_small = sum_small + 1
            break
print()
print('Во введённой строке найдено букв:')
print('Прописных:', sum_big)
print('Строчных:', sum_small)
