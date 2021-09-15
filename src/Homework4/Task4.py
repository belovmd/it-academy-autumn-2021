"""Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
"""
def list_difference():
    lst1 = [1, 3, 4, 6, 8, 10, 11, 12, 13, 15, 98, 45, 34, 21, 46, 36, 4, 9, 7, 10]
    lst2 = [i for i in range(21)]
    set1, set2 = set(lst1), set(lst2)
    print((set1 ^ set2), "=>", len(set1 ^ set2))

if __name__ == "__main__":
    list_difference()