#!/usr/bin/env python3


def unique_words_count(arr):
    return len(set(arr))


def main():
    print(unique_words_count(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
    main()
