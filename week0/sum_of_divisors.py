#!/usr/bin/env python3


def sum_of_divisors(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    divisors_sum = 0
    for i in divisors:
        divisors_sum += i
    return divisors_sum


def main():
    print(sum_of_divisors(18))

if __name__ == '__main__':
    main()
