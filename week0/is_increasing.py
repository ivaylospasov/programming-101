#!/usr/bin/env python3


def is_increasing(seq):
    seq_copy = seq[:]
    seq_copy.sort()
    if seq == seq_copy:
        return True
    else:
        return False


def main():
    print(is_increasing([-2, 0, 7, 15]))

if __name__ == '__main__':
    main()
