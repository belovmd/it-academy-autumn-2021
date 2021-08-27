def func(a, b):
  print(a + b)


# Вызываем функцию.
a = func(1, 2.5)
print(func(1, 2.5))


a, b = [], []

print(a+b)
a.extend(b)
print(a)

def very_big_func(a, b, *args, c, d=1, **kwargs):
  print(a, b, args, c, d, kwargs)

very_big_func(1, 2, 3, c=5, e=7)


def func(a=[]):
    if not a:
      a = []

    a += [1]
    return a

obj = []
print(id(obj))
print(id(func(obj)))

print(func(obj))
print(func(obj))
print(func(obj))



print("----")

def func1(a=[]):
    if a:
      a = []

    a += [1]
    return a

print(func1())
print(func1())
print(func1())



def func(a):
  print(a, type(a))

def fun_func():
  print('fun')

func(fun_func)

def func(a):
  print(a, type(a))

def fun_func():
  print('fun')
  return

func(fun_func())


# Стандартный способ обработки таких ситуаций(и заодно пример boilerplate кода).

# Изменяемое значение по умолчанию.
def func(a=None):
    if a is None:
        a = []

    a += [1]
    return (a)


print(func())
print(func())
print(func())

obj = []
print(id(obj))
print(id(func(obj)))

# Проверка 'if' a будет в большинстве случаев недостаточна, потому что нам может
# быть передан пустой список, и наш код в таком случае его перезапишет другим.