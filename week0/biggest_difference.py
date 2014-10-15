#!/usr/bin/env python3


def biggest_difference(arr):
    arr.sort()
    return arr[0] - arr[-1]


def main():
    print(biggest_difference([-2, 0, -7, 5]))

if __name__ == '__main__':
    main()
