#!/usr/bin/env python3


class CashDesk:

    def __init__(self, money={100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money

    def take_money(self, money_to_take):
        print(self.money)
        for note in money_to_take:
            existing_note_count = self.money[note]
            #print('There are {0} note(s) of {1} dolar'.format(existing_note_count, note))
            #print('Take {0} note(s) of {1} dolar'.format(money_to_take[note], note))
            count_to_take = money_to_take[note]
            if count_to_take <= existing_note_count:
                self.money[note] -= count_to_take
            else:
                print('You do not have the exact number of specific notes')
        return self.money

    def total(self):
        total_money = 0
        for note in self.money:
            available_from_every_note = self.money[note] * note
            total_money += available_from_every_note
        #print('Total money: ', total_money)
        return total_money

    def can_withdraw_money(self, amount_of_money):
        print(self.money)
        print(self.total())
        if self.total() >= amount_of_money:
            return True
        else:
            return False

my_cash_desk = CashDesk({100: 0, 50: 2, 20: 3, 10: 4, 5: 5, 2: 6, 1: 7})

my_cash_desk.take_money({1: 3, 50: 2, 20: 2})

my_cash_desk.total()  # 72

my_cash_desk.can_withdraw_money(101)

#my_cash_desk.can_withdraw_money(70) #True
