"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"."""
# my_string = 'The Ultimate Question of Life, the Universe, and Everything!..'
my_string = input('Input the string: ')
my_string = my_string.replace(' ', '')
new_string = my_string[0]
for i in range(0, len(my_string)):
    if my_string[i] not in new_string:
        new_string += my_string[i]
    else:
        new_string = new_string
print(new_string)
