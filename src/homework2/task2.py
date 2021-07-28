# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.

string_ = (input("Ввведите строку:"))
marks = ".,?-_:;!()/ "
for i in marks:
    string_ = string_.replace(i, " ")
words = string_.split()
print(max(words, key=len))
