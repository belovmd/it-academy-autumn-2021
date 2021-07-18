# print('Hello, world!')
num = int(input('Введите число число: '))
if num < 0:
    num = abs(num)
else:
    pass
rev = 0
head = num
while head:
    last_num = head % 10
    rev = rev * 10 + last_num
    head = (head // 10)
if num == rev:
    print("Палиндром")
else:
    print("Не палиндром")

