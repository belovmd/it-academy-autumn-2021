'''Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. Учитывать только английские буквы.
'''
text_input = input('Kindly input some English text: ')
count_lowercase = 0
count_uppercase = 0
print("The length of the text input is {} symbols". format(len(text_input)))  # this line had been added in order to check that the program works properly
for i in text_input:
    a = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    if i in a and i != a:
        count_lowercase += 1
    else:
        count_uppercase += 1
print("The count of the letters in lowercase is {}, the count of the letters in uppercase is {}".format(count_lowercase, count_uppercase))