# 11 lines: Triple-quoted strings, while loop
if __name__ == '__main__':
    REFRAIN = '''
    %d bottles of beer on the wall,
    %d bottles of beer,
    take one down, pass it around,
    %d bottles of beer on the wall!
    '''

    bottles_of_beer = 9
    while bottles_of_beer > 1:
        print(REFRAIN % (bottles_of_beer, bottles_of_beer,
                         bottles_of_beer - 1))
        bottles_of_beer -= 1
