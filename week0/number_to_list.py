#!/usr/bin/env python3


def number_to_list(n):
    nlist = [int(x) for x in str(n)]
    return nlist


def main():
    print(number_to_list(23425345))

if __name__ == '__main__':
    main()
