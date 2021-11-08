''' Создайте декоратор, который хранит результаты вызовов функции
    (за все время вызовов, не только текущий запуск программы)
'''


def decorator(funk):
    def wrapper(*args, **kwargs):
        result = funk(*args, **kwargs)
        with open('memorise.txt', 'a') as file:
            file.write('function result: ' + str(result) + '\n')
    return wrapper


@decorator
def naming(a):
    return a
