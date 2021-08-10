# Посчитать количество строчных (маленьких)
# и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

text_input = input('Kindly input some English text: ')
count_lowercase = 0
count_uppercase = 0
#  checking purposes
print("The length of the text input is {} symbols". format(len(text_input)))
for i in text_input:
    a = 'a', 'b', 'c', 'd', 'e', 'f'
    c = 'g', 'h', 'i', 'j', 'k', 'l', 'm'
    b = 'n', 'o', 'p', 'q', 'r', 's'
    d = 't', 'u', 'v', 'w', 'x', 'y', 'z'
    alphabet = a + b + c + d
    if i in alphabet and i != alphabet:
        count_lowercase += 1
    else:
        count_uppercase += 1
print("The count of the letters in lowercase is {}, "
      "the count of the letters in uppercase is {}".format(count_lowercase, count_uppercase))
