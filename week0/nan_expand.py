#!/usr/bin/env python3


def nan_expand(times):
    not_a = "Not a " * times
    return "{0}NaN".format(not_a)


def main():
    print(nan_expand(3))

if __name__ == '__main__':
    main()
