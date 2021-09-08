"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"."""
my_string = input('Input the string: ')
my_string = my_string.replace(' ', '')
new_string = my_string[0]
template = "The string of unique symbols is : {new_string}"
for i in range(len(my_string)):
    if my_string[i] not in new_string:
        new_string += my_string[i]
    else:
        new_string = new_string
print(template.format(new_string=new_string))
