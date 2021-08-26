# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.

string_ = (input("Ввведите строку:"))
for i in string_:
    if not i.isalnum():
       string_ = string_.replace(i, " ")
words = string_.split()
print(max(words, key=len))
