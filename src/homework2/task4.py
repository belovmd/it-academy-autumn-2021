'''Посчитать количество строчных (маленьких)
и прописных (больших) букв в введенной строке. Учитывать только английские буквы.
'''
str = (input(""))
str1 = str2 = 0
for x in str:
  if "a" <= x <= "z":
    str1 +=1
  else:
   if "A" <= x <= "Z":
    str2 +=1
print ("Количество маленьких",str1)
print ("Количество больших",str2)