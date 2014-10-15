#!/usr/bin/env python3


def is_prime(n):
    if n == 1:
        return False
    else:
        divisors = [i for i in range(1, n) if n % i == 0]
        if len(divisors) == 1:
            return True
        else:
            return False


def main():
    print(is_prime(3))

if __name__ == '__main__':
    main()
