def clean_string(string: str) -> str:
    string = string.replace(' ', '')
    letters = []
    for letter in string:
        if letters.count(letter) == 0:
            letters.append(letter)
    clean_str = ''
    for letter in letters:
        clean_str += letter
    return clean_str


if __name__ == '__main__':
    input_string = input("Input your string: ")
    print(f"Clean string: {clean_string(input_string)}")
