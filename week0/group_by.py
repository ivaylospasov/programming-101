#!/usr/bin/env python3


def groupby(func, seq):
    number_types = {}
    for arg in seq:
        number_types_key = func(arg)
        if number_types_key not in number_types:
            number_types[number_types_key] = []
        number_types[number_types_key].append(arg)
    return number_types


def main():
    print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))

if __name__ == '__main__':
    main()
