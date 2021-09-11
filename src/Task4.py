import os
import zipfile

path = "/Users/Roman/Desktop/IT-academy-2021/ratings.list"
directory = "/Users/Roman/Desktop/IT-academy-2021"
print(os.path.abspath("ratings.list.zip"))

"""with zipfile.ZipFile("/Users/Roman/Desktop/IT-academy-2021/ratings.list.zip", 'r') as zf:
    zf.extractall("/Users/Roman/Desktop/IT-academy-2021")
print("dezipping")"""

"""with open(path, 'r', encoding="Windows-1252") as f:
    flag = index = 0
    find = "top"
    for line in f:
        if find in line:
            print(line, "=>", index)
            flag = 1
            break
        else:
            print("Not found")
            break"""

