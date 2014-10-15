#!/usr/bin/env python3

from sys import argv
from random import randint

file = open(argv[1], "w")
number = int(argv[2])


def rand_numbers(number):
    rlist = []
    for num in range(number):
        rlist.append(str(randint(1, number)))
    rand_num_string = " ".join(rlist)
    return rand_num_string

contents = rand_numbers(number)

file.write(contents)

file.close()


def main():
    pass

if __name__ == '__main__':
    main()
