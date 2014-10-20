#!/usr/bin/env python3


def biggest_difference(arr):
    arr.sort()
    return arr[0] - arr[-1]
