''' Даны два списка чисел.
Посчитайте, сколько различных чисел содержится одновременно
как в первом списке, так и во втором.
'''

lst1 = [1, 5, 3, 7, 45, 32, 2]
lst2 = [4, 1, 5, 6, 8, 45, 36, 0]
print(len(set(lst1) ^ set(lst2)))
