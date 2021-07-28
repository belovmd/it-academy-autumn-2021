"""  Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
     Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""
str_ = (input("Введите cтроку: "))
new_str = ''
for i in str_:
    if i not in new_str and i != ' ':
        new_str += i
print(new_str)
