#!/usr/bin/env python3


def prepare_meal(number):
    spam = 'spam '
    eggs = 'eggs'
    and_eggs = 'and '
    spam_and_eggs = {spam: 0, and_eggs: 0, eggs: 0}
    for n in range(abs(number)):
        if number % (3 ** n) == 0:
            spam_and_eggs[spam] = n
    if number % 5 == 0:
        spam_and_eggs[eggs] = 1
    if spam_and_eggs[spam] and spam_and_eggs[eggs] != 0:
        spam_and_eggs[and_eggs] = 1
    meal = (spam * spam_and_eggs[spam]) + (
        and_eggs * spam_and_eggs[and_eggs]) + (
        eggs * spam_and_eggs[eggs])
    return meal


def main():
    print(prepare_meal(45))

if __name__ == '__main__':
    main()

