# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

def fizz_buzz():
    digits = [i for i in range(1, 10)]
    new_list = []
    for item in digits:
        if item % 3:
            new_list.append('Fizz')
        if item % 5:
            new_list.append('Buzz')
        if (item % 3) and (item % 5):
            new_list.append('FizzBuzz')
        else:
            new_list.append(item)
    return new_list


def dct():
    return {int(x): (x ** 3) for x in range(1, 21)}


def lst():
    return [element1 + element2 for element1 in 'ab' for element2 in 'bcd']


def runner(*args):
    result = ''
    for el in args:
        result += str(el()) + '\n'
    return result


if __name__ == '__main__':
    print(runner(fizz_buzz, dct))
    print()
    print(runner(dct))
    print()
    print(runner(fizz_buzz, dct, lst))
