"""Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

string_ = "1 2 4 5 7 7 4 5 3 2 1 2 2 1 1 10 10 10 11 36 36 37 a a g g g n f j k l"
list_ = string_.split()
dict_ = dict.fromkeys(list_, 0)
l_ = len(list_)
i = 1
for k in list_:
    for j in list_[i:l_]:
        if k == j:
            dict_[k] += 1
    i += 1
print("Уникальные элементы в строке:\n" + " ".join("{}".format(k) for k, v in dict_.items() if not v))

