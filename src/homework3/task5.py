'''Дан список. Выведите те его элементы, которые встречаются в списке только
один раз. Элементы нужно выводить в том порядке, в котором они встречаются
в списке.
'''

# lst = [int(s) for s in input().split()]
lst = [1, 5, 2, 56, 3, 1, 3, 1, 7, 1]
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j and lst[i] == lst[j]:
            break
    else:
        print(lst[i], end=' ')
