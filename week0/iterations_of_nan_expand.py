#!/usr/bin/env python3

from counting_substrings import count_substrings


def iterations_of_nan_expand(expanded):
    if count_substrings(expanded, "Not a") == 0:
        print("No 'Not a' in the string")
        return False
    else:
        return count_substrings(expanded, "Not a")


def main():
    print(iterations_of_nan_expand('Not a Not a Not a Not a Not a NaN'))

if __name__ == '__main__':
    main()
