#!/usr/bin/env python3

consonants = 'bcdfghjklmnpqrstvwxz'


def count_consonants(str):
    lower_string = str.lower()
    count = 0
    for char in consonants:
        count += lower_string.count(char)
    return count


def main():
    print(count_consonants('Theistareykjarbunga'))

if __name__ == '__main__':
    main()
