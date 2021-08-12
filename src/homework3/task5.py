# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

lst = [int(x) for x in input('List: ').split()]
unique_list = []
for el in lst:
    if el not in unique_list:
        unique_list.append(el)
print('Unique list: ', unique_list)
