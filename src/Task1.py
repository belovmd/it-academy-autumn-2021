def generators():
    list_ = [i + k for i in 'abc' for k in 'abc']
    list_2 = list_[1::2]
    list_3 = [str(i) + 'a' for i in range(1, 5)]
    print(f"list_ => {list_}")
    print(f"list_2 => {list_2}")
    el = list_3.pop(1)
    print(f"list_3 => {list_3} => element {el} popped")
    list_4 = list_3[:]
    list_4.insert(1, el)
    print(f"list_4 => {list_4} <= element {el} inserted")


if __name__ == '__main__':
    generators()
