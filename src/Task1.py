import os
import pkgutil
import Homework2
from Homework3 import Task1

lst_ = [f for f in os.listdir("/Users/Roman/Desktop/IT-academy-2021/it-academy-autumn-2021/src")
        if f.startswith('Home')]

dct_ = {el: [f for f in os.listdir(el) if not f.startswith('__')] for el in lst_}
print(dct_)

#info = list(pkgutil.iter_modules("src"))
#print(info)
for v in dct_.values():
    for val in v:
        print(dir(val))

"""for v in dct_.values():
    for val in v:
        __import__(val[:-3])"""

all = list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname("src")]))
print(all)

# print(lst_)
# print(lst_1)
print(type(Homework2))
a = [el for el in dir(Task1) if not el.startswith("__")]
print(a)

from Task1 import function((a[0]))
