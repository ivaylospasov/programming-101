#!/usr/bin/env python3


def contains_digits(number, digits):
    for a in digits:
        if a not in number:
            return False
    return True


def main():
    print(contains_digits([4, 0, 2, 1, 2, 3], [0, 3, 4]))

if __name__ == '__main__':
    main()
