"""List practice
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список из прошлого пункта и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""


def generators():
    # Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    list_1 = [i + k for i in 'abc' for k in 'bcd']

    # Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc']
    list_2 = list_1[::2]

    # Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
    list_3 = [str(i) + 'a' for i in range(1, 5)]

    # Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
    el = list_3.pop(1)

    # Скопируйте список из прошлого пункта и добавьте в него элемент '2a'
    # так чтобы в исходном списке этого элемента не было.
    list_4 = list_3[:]
    list_4.insert(1, el)

    print(f"list_1 => {list_1}")
    print(f"list_2 => {list_2}")
    print(el)
    print(f"list_3 => {list_3} => element {el} popped")
    print(f"list_4 => {list_4} <= element {el} inserted")


if __name__ == '__main__':
    generators()
