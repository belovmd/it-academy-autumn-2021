import sys


if __name__ == '__main__':
    try:
        total = sum(int(arg) for arg in sys.argv[1:])
        print('sum =', total)
    except ValueError:
        print('Please supply integer arguments')
