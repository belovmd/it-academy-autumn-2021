""""Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
lst_ = []
lst_dub = []
str_ = input('Input your elements: ')
str_ = str_.strip()
str_ = str_.split(' ')
for el in str_:
    lst_.append(el)
print(lst_)
for i in lst_:
    if i not in lst_dub:
        lst_dub.append(i)
print(lst_dub)
