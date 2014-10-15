#!/usr/bin/env python3


def sevens_in_a_row(arr, n):
    sevens = [x for x in arr if x == 7]
    if n > 0 and len(sevens) >= n:
        return True
    else:
        return False

print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
