#!/usr/bin/env python3


def is_an_bn(word):
    if len(word) == 0:
        return True
    else:
        alist = [word[char] for char in range(len(word) // 2)]
        blist = [word[char] for char in range(len(word) // 2, len(word))]
        if (len(alist) == len(blist)) and (set(alist) == {'a'} and set(blist) == {'b'}):
            return True
        else:
            return False


def main():
    print(is_an_bn(''))

if __name__ == '__main__':
    main()
