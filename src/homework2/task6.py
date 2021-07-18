num = int(input('Введите число число: '))
rev = 0
n = num
while n:
    last_num = n % 10
    rev = rev * 10 + last_num
    n = (n // 10)
if num == rev:
    print("Палиндром")
else:
    print("Не палиндром")
