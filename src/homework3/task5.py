""" 5 Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
Задачу поместите в файл task5.py в папке src/homework3.
"""

input_list = [0, 2, 5, 7, 45, 23, 0, 7, 8, 100, 34, 36, 2]
print(input_list)

for i in range(len(input_list)):
    for j in range(len(input_list)):
        if not i == j:  # исключение проверки самого себя
            if input_list[i] == input_list[j]:
                break
            elif j == len(input_list) - 1:
                print(input_list[i], end=' ')
