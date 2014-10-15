#!/usr/bin/env python3

import os
from datetime import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def cat(filename):
    file = open(filename, 'r')
    content = file.read()
    print(bcolors.OKGREEN + '\nLoading ' + filename)
    print(bcolors.WARNING + '\n' + content + bcolors.ENDC)
    file.close()


def pizza():
    finish = 'no'
    name_and_price = {}

    while finish == 'no':
        print('\nMenu Selections: ')
        print('1-Take: ')
        print('2-Status: ')
        print('3-Save: ')
        print('4-List: ')
        print('5-Load')
        print('6-Finish')

        choice = input('\nEnter your selection: ')
        if choice == '1':
            name = input(bcolors.WARNING + '\nPlease, enter name: ')
            price = input('Please, enter price: ')
            if name in name_and_price:
                name_and_price[name] += float(price)
                print(bcolors.OKBLUE + '\nTaking order form {0} for {1}'.format(
                    name, price) + bcolors.ENDC)
            else:
                name_and_price[name] = float(price)
                print(bcolors.OKBLUE + '\nTaking order form {0} for {1}'.format(
                    name, price) + bcolors.ENDC)

        elif choice == '2':
            print(bcolors.FAIL + '\nUnsaved')
            for key in name_and_price.keys():
                print(bcolors.FAIL + '{0} - {1}'.format(
                    key, name_and_price[key]) + bcolors.ENDC)

        elif choice == '3':
            time_now = datetime.now()
            stamp = time_now.strftime('%Y_%m_%d_%H_%M_%S')
            filename = 'orders_{0}'.format(stamp)
            orders_list = []
            for key in name_and_price.keys():
                orders_string = str(key) + ' - ' + str(name_and_price[key])
                orders_list.append(orders_string)
            file = open(filename, "w")
            contents = orders_list
            file.write("\n".join(contents))
            file.close()
            name_and_price = {}

        elif choice == '4':
            files = sorted([f for f in os.listdir('.') if f.startswith('orders_')])
            if len(files) == 0:
                print(bcolors.FAIL + "\nThere are no saved orders." + bcolors.ENDC)
            else:
                print(bcolors.OKGREEN + '\nSaved orders:' + bcolors.ENDC)
                for index, order in enumerate(files):
                    print(bcolors.OKBLUE + str([index + 1]) + ' - ' + order + bcolors.ENDC)

        elif choice == '5':
            if len(name_and_price) != 0:
                print('\nYou have unsaved order.\
                    \nIf you wish to discard the current order, type "load"')
                load_choice = input('Enter commmand: ')
                if load_choice == 'load':
                    name_and_price = {}
                    choosen_file = input('Choose file to open: ')
                    cat(files[int(choosen_file)-1])
            else:
                choosen_file = input('Choose file to open: ')
                cat(files[int(choosen_file)-1])
        elif choice == '6':
            finish = 'yes'
            print('Thank you!')
        else:
            print(bcolors.WARNING + '\nUnknown command!\
                \nTry one of the following:' + bcolors.ENDC)


def main():
    pizza()

if __name__ == '__main__':
    main()
