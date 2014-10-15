#!/usr/bin/env python3

from sum_of_digits import sum_of_digits


def is_number_balanced(n):
    nstring = str(abs(n))
    nlength = len(nstring)
    halflength = nlength // 2
    firsthalf = [nstring[i] for i in range(halflength)]
    x = int(''.join(firsthalf))
    if nlength == 1:
        return True
    else:
        if nlength % 2 == 0:
            secondhalf = [nstring[i] for i in range(halflength, nlength)]
            y = int(''.join(secondhalf))
            if sum_of_digits(x) == sum_of_digits(y):
                return True
            else:
                return False
        else:
            secondhalf = [nstring[i] for i in range((halflength+1), nlength)]
            y = int(''.join(secondhalf))
            if sum_of_digits(x) == sum_of_digits(y):
                return True
            else:
                return False


def main():
    print(is_number_balanced(-12345650145))

if __name__ == '__main__':
    main()
