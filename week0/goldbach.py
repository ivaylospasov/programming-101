#!/usr/bin/env python3

from is_prime import is_prime


def goldbach(n):
    numbers = [(x, y) for x in range(1, n)
               for y in range(1, n)
               if is_prime(x)  # True
               if is_prime(y)  # True
               if x <= y
               if (x + y) == n]
    return numbers


def main():
    print(goldbach(52))

if __name__ == '__main__':
    main()
