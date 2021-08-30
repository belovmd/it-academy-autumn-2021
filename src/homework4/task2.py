'''Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.'''

dct = {}
for v in range(int(input())):
    n = input().split()
    country, cityes = n[0], n[1:]
    for c in cityes:
        dct[c] = country
for i in range(int(input())):
    print(dct[input()])
