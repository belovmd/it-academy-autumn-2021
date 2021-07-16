# 20 lines: Prime numbers sieve w/fancy generators
import itertools


def iter_primes():
    numbers = itertools.count(2)
    # generate primes forever
    while True:
        # get the first number from the iterator (always a prime)
        prime = next(numbers)
        yield prime

        # this code iteratively builds up a chain of
        # filters...slightly tricky, but ponder it a bit
        numbers = filter(prime.__rmod__, numbers)


if __name__ == '__main__':
    for p in iter_primes():
        if p > 1000:
            break
        print(p)
