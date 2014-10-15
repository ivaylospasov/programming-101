#!/usr/bin/env python3

vowels = 'aeiouy'


def count_vowels(str):
    lower_string = str.lower()
    count = 0
    for char in vowels:
        count += lower_string.count(char)
    return count


def main():
    print(count_vowels('Theistareykjarbunga'))

if __name__ == '__main__':
    main()
