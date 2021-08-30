"""
Даны два списка чисел. Посчитайте, сколько различных чисел
входит только в один из этих списков
"""

lst_1 = [int(element) for element in input().split()]
lst_2 = [int(element) for element in input().split()]
set_of_lst = set(lst_1) - set(lst_2)
print(len(set_of_lst))
