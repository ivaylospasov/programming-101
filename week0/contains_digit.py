#!/usr/bin/env python3


def contains_digit(number, digit):
    if str(digit) in str(number):
        return True
    else:
        return False


def main():
    print(contains_digit(1234, 4))

if __name__ == '__main__':
    main()
