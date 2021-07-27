# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
import re


def find_word_with_max_len(sentence: str) -> str:
    words = re.split(r'[,!?:; .-]', sentence)
    result_word = ''
    for word in words:
        if len(word) > len(result_word):
            result_word = word
    return result_word


if __name__ == '__main__':
    input_sentence = input("Input your sentence: ")
    print(f"Word with max len {find_word_with_max_len(input_sentence)}")
