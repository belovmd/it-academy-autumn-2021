"""
Dict comprehensions
Создайте словарь с помощью генератора словарей, так
чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
Задачу поместите в файл task1.py в папке src/homework4.
"""

a = {el: el ** 3 for el in range(1, 21)}

for el in a:
    print(el, ':', a[el])
