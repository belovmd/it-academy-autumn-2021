# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
#  Например, если было введено "abc cde def", то должно быть выведено "abcdef".

string_ = input("Введите строку:")
fixstring = ""
string1 = string_.replace(" ", "")

for i in string1:
    if i not in fixstring:
        fixstring += i
print(fixstring)
