#!/usr/bin/env python3


def ExOH(word):
    x_list = [letter for letter in word if letter == 'x']
    o_list = [letter for letter in word if letter != 'x']
    if len(x_list) == len(o_list):
        return True
    else:
        return False


def main():
    print(ExOH('xoxoox'))
    print(ExOH('oooxoo'))

if __name__ == '__main__':
    main()
