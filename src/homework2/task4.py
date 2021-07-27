"""Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
my_string = 'Главный вопрос Жизни, Вселенной и вообще!..
The Ultimate Question of Life, the Universe, and Everything!..'
"""
my_string = input('Input the string: ')
template = "\nNumber of uppercase latin letters : {upper_case} \nNumber of lowercase latin letters : {lower_case}"
upper_case = 0
lower_case = 0
latin_alph_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
latin_alph_lower = latin_alph_upper.lower()
for symbol in my_string:
    if symbol in latin_alph_upper:
        upper_case += 1
    if symbol in latin_alph_lower:
        lower_case += 1
print(template.format(upper_case=upper_case, lower_case=lower_case))
