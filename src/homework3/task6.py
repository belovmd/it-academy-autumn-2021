# Упорядоченный список.
# Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
list_ = [1, 2, 0, 2, 0, 4, -1, 3]
for num in range(len(list_)):
    if not list_[num]:
       list_.append(list_.pop(num))
print(list_)
