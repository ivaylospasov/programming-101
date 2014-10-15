#!/usr/bin/env python3

from sys import argv
from is_prime import is_prime

number = argv[1]


def prime_factorization(number):
    int_number = int(number)
    prime_with_greater_power = {}
    result = []
    prime_dividers = [x for x in range(1, int_number+1)
                      if is_prime(x) is True
                      if int_number % x == 0]
    print("The prime dividers of {0} are {1}".format(
          int_number, prime_dividers))
    prime_and_power_pairs = [(i, n)
                             for i in prime_dividers
                             for n in range(1, int_number)
                             if int_number % (i**n) == 0]
    for idx, pair in enumerate(prime_and_power_pairs):
        prime_with_greater_power[pair[0]] = pair[1]
    for i in prime_with_greater_power.items():
        result.append(i)
    return result


def main():
    print(prime_factorization(argv[1]))

if __name__ == '__main__':
    main()
