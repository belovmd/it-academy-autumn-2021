''' Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы) '''


def dec(fun):
    def wrapper(arg):
        i = 0
        result = fun(arg) + i
        fh = open('result.txt', 't')
        fh.write(str(result) + '\n')
        fh.close

        return result

    return wrapper


@dec
def func(t):
    return t


print(func(1))
print(func(2))
print(func(3))
