#!/usr/bin/env python3


def nth_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)


def main():
    print(nth_fibonacci(7))

if __name__ == '__main__':
    main()
