""" Найти самое длинное слово  в введенном  предложении.
    Учтите что в предложении есть знаки препинания.
"""
str_ = (input("Введите предложение: "))
punktuation = ",.?!-:;"
for mark in punktuation:
    str_ = str_.replace(mark, "")
words = str_.split(" ")
longest_word = " "
for word in words:
    if len(word) + len(longest_word):
        longest_word = word
print("Самое длинное слово -", longest_word)
