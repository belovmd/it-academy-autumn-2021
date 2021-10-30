"""Создайте декоратор, который хранит результаты
вызовов функции (за все время вызовов, не только текущий запуск программы)
"""


def dec(func):
    n = open('save.txt', 'a')
    n.close()

    def wrapper():
        nonlocal n
        n = open('save.txt', 'a')
        n.write('1')
        n.close()
        n = open('save.txt')
        line = n.read()
        numlist = list(line)
        r = [int(intem) for intem in numlist]
        vizovi = str(sum(r))
        n.close()
        n = open('save.txt', 'w')
        n.write(vizovi)
        print(vizovi, 'вызовов')
        n.close()
        result = func()
        return result

    return wrapper


@dec
def cost():
    print('за все время')
