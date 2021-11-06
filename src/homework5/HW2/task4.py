"""Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы."""


def quantity_upper_lower_case_letters():
    my_string = input('Input the string: ')
    template = "Number of uppercase latin letters : {upper_case} " \
               "\nNumber of lowercase latin letters : {lower_case}"
    upper_case = 0
    lower_case = 0
    for symbol in my_string:
        if str.isupper(symbol) and 'A' <= symbol <= 'Z':
            upper_case += 1
        if str.islower(symbol) and 'a' <= symbol <= 'z':
            lower_case += 1
    print(template.format(upper_case=upper_case, lower_case=lower_case))
    return print()
