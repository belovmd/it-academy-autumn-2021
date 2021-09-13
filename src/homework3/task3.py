# Tuple practice
# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
list_ = [symbol_ for symbol_ in 'abc']
print('список', list_)
tuple_ = tuple(list_)
print('кортеж', tuple_)

# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
tuple_ = ('a', 'b', 'c')
print('кортеж', tuple_)
list_ = list(tuple_)
print('список', list_)

# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
a, b, c = 'a', 2, 'python'
print(a, b, c)

# Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно
# выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
tuple_1 = ([1, 2, 3], )
print('длина кортежа: ', len(tuple_1))
for element in tuple_1[0]:
    print(element, ', длина кортежа:', len(tuple_1))
