#!/usr/bin/env python3


def dividers(n):
    dividers = [x for x in range(n, 0, -1) if n % x == 0]
    return dividers


def simplify_fraction(fraction):
    x, y = fraction
    division_list = [(int(x / i), int(y / i)) for i in dividers(x)
                     if (x % i == 0 and y % i == 0)]
    return division_list[0]


def main():
    print(simplify_fraction((63, 462)))

if __name__ == '__main__':
    main()
