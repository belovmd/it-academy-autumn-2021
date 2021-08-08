def crazy_function():
    list_ = []
    for i in range(1, 101):
        if not i % 3:
            list_.append('Fizz')
        elif not i % 5:
            list_.append('Buzz')
        elif not i % 3 and i % 5:
            list_.append('FizzBuzz')
        else:
            list_.append(i)
    return list_


if __name__ == '__main__':
    print(crazy_function())
