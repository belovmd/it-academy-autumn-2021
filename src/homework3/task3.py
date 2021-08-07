"""Tuple practice
1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
"""
first_lst = ['a', 'b', 'c']
first_tupl = tuple(first_lst)


"""
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
"""
second_tupl = ('a', 'b', 'c')
second_lst = list(second_tupl)


"""
3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’
"""
a, b, c = 'a', 2, 'python'
print(a, b, c)


"""
4. Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементы последовательно выводились значения 1, 2, 3. Убедитесь
что len() исходного кортежа возвращает 1.
"""
last_tupl = ('123',)


print('len = ', len(last_tupl), 'type =', type(last_tupl))

for num in last_tupl[0]:
    print(num)
