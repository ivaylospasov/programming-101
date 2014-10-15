#!/usr/bin/env python3

from sys import argv

for index in range(1, len(list(enumerate(argv)))):
    file = open(argv[index])
    content = file.read()
    print(content, end='\n\n')
    file.close()


def main():
    pass

if __name__ == '__main__':
    main()
