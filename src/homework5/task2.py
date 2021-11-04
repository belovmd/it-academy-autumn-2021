# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

def dec(fun):
    def wrapper(arg):
        i = 0
        result = fun(arg) + i
        fh = open('result.txt', 'a')
        fh.write(str(result) + '\n')
        fh.close

        return result

    return wrapper


@dec
def func(b):
    a = b + 5
    return a


print(func(15))
