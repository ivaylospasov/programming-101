#!/usr/bin/env python3

from is_int_palindrome import is_int_palindrome


def hack_numbers(n):
    binary_n = bin(n)
    binary_string = binary_n[2:]
    print("The binary of number {0} is {1}".format(n, binary_n))
    count_ones = 0
    for i in binary_string:
        if int(i) == 1:
            count_ones += 1
    print("{0} has {1} times number 1 in it".format(binary_n, count_ones))
    if is_int_palindrome(int(binary_string)) is True and count_ones % 2 != 0:
        print("{0} is palindrom".format(binary_n))
        print("{0} is a hack number".format(n))
        return True
    else:
        n += 1
        hack_numbers(n)


def main():
    print(hack_numbers(18))

if __name__ == '__main__':
    main()
