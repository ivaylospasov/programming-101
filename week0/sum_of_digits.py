#!/usr/bin/env python3


def sum_of_digits(n):
    digits = [int(i) for i in str(abs(n))]
    count = 0
    for number in digits:
        count += number
    return count


def main():
    print(sum_of_digits(-1323132435326))

if __name__ == '__main__':
    main()
