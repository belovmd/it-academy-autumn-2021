# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится


def calculate_fibonachi_value(number: int) -> int:
    first_element = 0
    second_element = 1
    if number == 0:
        return first_element
    if number == 1:
        return second_element
    if number == 2:
        return first_element + second_element
    fibonachi_values = [first_element, second_element]
    for index in range(2, number - 1):
        value = fibonachi_values[index - 2] + fibonachi_values[index - 1]
        fibonachi_values.append(value)
    return sum(fibonachi_values) + 1


if __name__ == '__main__':
    n = int(input("Input number of fibonachi value: "))
    print(f"{n} value of fibonachi is {calculate_fibonachi_value(n)}")
