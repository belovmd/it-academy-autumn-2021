# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
lst1 = [element1 + element2 for element1 in 'ab' for element2 in 'bcd']
print(lst1)

# Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
print(lst1[::2])

# Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
new_list = [element1 + 'a' for element1 in '1234']
print(new_list)

# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
print(new_list.pop(1))

# Скопируйте список из прошлого пункта и добавьте в него элемент '2a'
# так чтобы в исходном списке этого элемента не было.
the_list = new_list.copy()
print('the list without 2a: ', new_list)
print('the copied list: ', the_list)
the_list.insert(1, '2a')
print('when inserted: ', the_list)
print('there is still no 2a in the list: ', new_list)
