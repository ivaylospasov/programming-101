#!/usr/bin/env python3

from is_prime import is_prime


def prime_number_of_divisors(n):
    divisors = [x for x in range(1, n+1) if n % x == 0]
    if is_prime(len(divisors)) is True:
        return True
    else:
        return False


def main():
    print(prime_number_of_divisors(45))

if __name__ == '__main__':
    main()
