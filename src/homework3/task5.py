# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

def pairs(lst):
    print('The list: ', lst)
    print('Unique elements: ')
    for el in lst:
        if lst.count(el) == 1:
            print(el)

lst = [21, 25, 84, 65, 23, 24, 12, 21, 84]
pairs(lst)
