'''Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a'
 так чтобы в исходном списке этого элемента не было.'''

s = 'abcd'
lst = [s[x] + s[z] for x in range(2) for z in range(1, 4)]
print(lst)
lst1 = lst[::2]
print(lst1)
lst2 = [str(u) + "a" for u in range(1, 5)]
print(lst2)
print(lst2.pop(1))
lst3 = lst2.copy()
lst3.insert(1, '2a')
print(lst3, lst2)
