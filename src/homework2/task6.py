def reverse_number(number: int) -> int:
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    return reverse


def is_palindrome(number: int) -> bool:
    rev_number = reverse_number(number)
    return rev_number == number


if __name__ == '__main__':
    n = int(input("Input your number: "))
    if is_palindrome(n):
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not palindrome")
