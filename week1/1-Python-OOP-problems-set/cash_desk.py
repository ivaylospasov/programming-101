#!/usr/bin/env python3

import copy


class CashDesk:

    def __init__(self, money={100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money

    def take_money(self, money_to_take):
        for note in money_to_take.keys():
            available_notes_count = self.money[note]
            notes_count_to_take = money_to_take[note]
            if notes_count_to_take <= available_notes_count:
                self.money[note] -= notes_count_to_take

    def total(self):
        total_money = 0
        for note in self.money.keys():
            available_from_every_note = self.money[note] * note
            total_money += available_from_every_note
        return total_money

    def can_withdraw_money(self, amount):
        copy_available_money = copy.deepcopy(self.money)
        for note in sorted(copy_available_money.keys(), reverse=True):
            while copy_available_money[note] > 0 and amount - note >= 0:
                amount -= note
                copy_available_money[note] -= 1
        if amount > 0:
            return False
        return True


def main():
    my_cash_desk = CashDesk({100: 0, 50: 2, 20: 3, 10: 4, 5: 5, 2: 6, 1: 7})

    my_cash_desk.take_money({1: 3, 50: 3, 20: 2})

    my_cash_desk.total()  # 72

    print(my_cash_desk.can_withdraw_money(100))

    print(my_cash_desk.can_withdraw_money(270))


if __name__ == '__main__':
    main()
