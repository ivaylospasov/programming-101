#!/usr/bin/env python3


def zero_insert(n):
    digits_list = list(str(n))
    index_list = []
    for i in range(len(digits_list)):
        if digits_list[i] == digits_list[i-1] or ((int(digits_list[i]) + int(digits_list[i-1])) % 10 == 0):
            index_list.append(i)
    index_list.sort(reverse=True)
    for i in index_list:
        digits_list.insert(i, '0')
    n_with_zeros = int(''.join(digits_list))
    return(n_with_zeros)


def main():
    print(zero_insert(1136466377))

if __name__ == '__main__':
    main()
