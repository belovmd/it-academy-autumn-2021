""""Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
lst_ = [1, 2, '#',  5, 2, 'lst', 5, '#', 'lst']
lst_dub = []
print(lst_)
for i in lst_:
    if i not in lst_dub:
        lst_dub.append(i)
print(lst_dub)
