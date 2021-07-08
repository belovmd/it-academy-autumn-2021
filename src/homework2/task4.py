from typing import Tuple


def calc_lower_and_upper_letters(string: str) -> Tuple[int, int]:
    upper_count = 0
    lower_count = 0
    for symbol in string:
        if not symbol.isalpha():
            continue
        if symbol.islower():
            lower_count += 1
        else:
            upper_count += 1
    return lower_count, upper_count


if __name__ == '__main__':
    input_string = input("Input your string: ")
    upper, lower = calc_lower_and_upper_letters(input_string)
    print(f"We have {upper} upper letters and {lower} lower letters.")
