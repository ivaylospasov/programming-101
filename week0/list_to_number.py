#!/usr/bin/env python3


def list_to_number(n):
    x = [str(i) for i in n]
    y = int(''.join(x))
    return y


def main():
    print(list_to_number([1, 3, 4, 2, 5, 3, 4, 5]))

if __name__ == '__main__':
    main()
