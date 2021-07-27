"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например,
если было введено "abc cde def", то должно быть выведено "abcdef".
"""

str_old = input('Введите строку с пробелами: ')
str_new = ''
for i in str_old:
    if i not in str_new and i != ' ':
        str_new += i
print(str_new)
