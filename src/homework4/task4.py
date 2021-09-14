# Даны два списка чисел.
# Посчитайте, сколько различных чисел входит только в один из этих списков
list_1 = [8, 1, 2, 5, 5, 3]
list_2 = [8, 8, 8, 3, 4, 1, 6]
set_1, set_2 = set(list_1), set(list_2)
new_set = set_1 ^ set_2
unique_num = 0
for i in new_set:
    unique_num += 1
print(new_set)
print(unique_num)
