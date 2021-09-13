# Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
list_ = (1, 1, 2, 3, 6, 4, 5, -1, 2, 'h')
for element in list_:
    if list_.count(element) == 1:
        print(element)

# если результать нужно вывести списком, тогда решение ниже:
list_ = (1, 1, 2, 3, 6, 4, 5, -1, 2, 'h')
unique_element = []
for element in list_:
    if list_.count(element) == 1:
        unique_element.append(element)
print(unique_element)
