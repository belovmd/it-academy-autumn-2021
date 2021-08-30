# Посчитать количество строчных (маленьких)
# и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

text = str(input())
count_lowercase = 0
count_uppercase = 0
for letter in text:
    if ord(letter) >= 65 and ord(letter) <= 90:
        count_uppercase += 1
    elif ord(letter) >= 97 and ord(letter) <= 122:
        count_lowercase += 1
print('The number of characters in upper case: ', count_uppercase,
      '\nThe number of characters in lower case: ', count_lowercase)
