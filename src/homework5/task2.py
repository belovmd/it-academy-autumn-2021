"""2. Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)"""


def decorator(func):
    all_result = []

    def wrapper(*args, **kwargs):
        nonlocal all_result
        all_result.append(func(*args, **kwargs))
        return all_result
    return wrapper


@decorator
def function(number, degree):
    return number ** degree


print(function(5, 2))
print(function(10, 3))
print(function(1, 3))
