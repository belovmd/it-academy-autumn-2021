"""List practice"""
import copy
# Получение ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
lst1 = [a + b for a in 'ab' for b in 'bcd']
# получение ['ab', 'ad', 'bc'] используя слайс
lst2 = lst1[::2]
# получение списка ['1a', '2a', '3a', '4a']
lst3 = [a + b for a in '1234' for b in 'a']  # получение списка ['1a', '2a', '3a', '4a']
# удаление '2a' из прошлого списка и его печать
lst4 = lst3.pop(1)
print(lst4)
# Копирование предыдущего списка и вставка  '2a', чтобы в исходном списке этого элемента не было
lst5 = copy.copy(lst3)
lst5.append('2a')
print(lst5)
