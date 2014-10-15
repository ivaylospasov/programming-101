#!/usr/bin/env python3


def count_substrings(haystack, needle):
    return haystack.count(needle)


def main():
    print(count_substrings("Python is an awesome programming language", "o"))

if __name__ == '__main__':
    main()
