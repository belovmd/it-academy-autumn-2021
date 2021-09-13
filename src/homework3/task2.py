# List practice
# Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список из прошлого пункта и добавьте в него элемент '2a' так чтобы в исходном списке
# этого элемента не было
import copy
list_ = [symbol_1 + symbol_2 for symbol_1 in 'ab' for symbol_2 in 'bcd']
print(list_)

print(list_[0::2])

alpha_num_list_ = [str(num) + 'a' for num in range(1, 5)]
print(alpha_num_list_)

print(alpha_num_list_.pop(1))

new_alpha_num_list_ = copy.copy(alpha_num_list_)
new_alpha_num_list_.insert(1, '2a')
print(alpha_num_list_)
print(new_alpha_num_list_)
