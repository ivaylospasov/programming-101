#!/usr/bin/env python3


def is_decreasing(seq):
    seq_copy = seq[:]
    seq_copy.sort(reverse=True)
    if seq == seq_copy:
        return True
    else:
        return False


def main():
    print(is_decreasing([10, 7, 0, -2]))

if __name__ == '__main__':
    main()
