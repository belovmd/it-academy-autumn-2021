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
def func(a):
    return a


print(func(1))
print(func(2))
print(func(3))
