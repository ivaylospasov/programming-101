#!/usr/bin/env python3


def is_int_palindrome(n):
    digits_list = [x for x in str(n)]
    if n == 1:
        return True
    else:
        digits_list.reverse()
        reversed_n = int(''.join(digits_list))
        if reversed_n == n:
            return True
        else:
            return False


def main():
    print(is_int_palindrome(111101101111))

if __name__ == '__main__':
    main()
