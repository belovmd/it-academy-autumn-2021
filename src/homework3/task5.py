"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


lst_ = [1, 3, 1, 1, 2, 2, 'a', 'b', 'b']

dct = {}
for element in lst_:
    dct[element] = dct.get(element, 0) + 1

output_lst = []
for key, value in dct.items():
    if value == 1:
        output_lst.append(key)

print(output_lst)
