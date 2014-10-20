#!/usr/bin/env python3


def calculate_coins(sum):
    COINS = [100, 50, 20, 10, 5, 2, 1]
    sum *= 100
    change = {}
    while sum > 0:
        for coin in COINS:
            if sum - coin >= 0:
                if coin in change:
                    change[coin] += 1
                else:
                    change[coin] = 1
                sum -= coin
                break
    return change
