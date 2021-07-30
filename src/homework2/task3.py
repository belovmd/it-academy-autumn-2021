"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"."""
str_ = input('Введите строку: ')
new_str = ' '

for x in str_:
    if x not in new_str:
        new_str += x

print(new_str)
