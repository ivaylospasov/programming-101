#!/usr/bin/env python3

from sys import argv

script, filename = argv


def cat(filename):
    file = open(filename, 'r')
    content = file.read()
    print(content)
    file.close()


def main():
    cat(filename)

if __name__ == '__main__':
    main()
