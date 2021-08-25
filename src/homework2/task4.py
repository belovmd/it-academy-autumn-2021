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

for s_index in range(0, len(s)):
    for letter_index in range(0, 26):
        if s[s_index] == Big_letters[letter_index]:
            sum_big += 1
            break
        elif s[s_index] == Small_letters[letter_index]:
            sum_small += 1
            break
print()
print('Во введённой строке найдено букв:')
print('Прописных:', sum_big)
print('Строчных:', sum_small)
