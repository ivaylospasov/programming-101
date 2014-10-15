#!/usr/bin/env python3

from sys import argv

filename = argv[1]

file = open(filename, 'r')
content = file.read()
list_numbers = content.split(' ')
count = 0
for idx, number in enumerate(list_numbers):
    count += int(number)
print(count)
file.close()


def main():
    pass

if __name__ == '__main__':
    main()
