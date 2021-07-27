"""
3. Вводится строка. Требуется удалить
из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def",
то должно быть выведено "abcdef"
"""

inp_str = input('Введите текст: ')

answer = ''

for i in inp_str:
    if i not in answer and i != ' ':
        answer += i

print(answer)
