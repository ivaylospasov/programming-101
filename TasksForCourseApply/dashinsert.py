#!/usr/bin/env python3


def DashInsert(num):
    y = list(str(num))
    # List backwards the indexes of the second element of odd numbers pair
    second_odd = [(x+1) for x in range((len(y)-1), -1, -1)
                  if ((int(y[x]) % 2 != 0) and (int(y[x+1]) % 2 != 0))]
    for i in second_odd:
        y.insert(i, '-')
    return ''.join(y)


def main():
    print(DashInsert(87345839273967923642567623453906472468234852332))

if __name__ == '__main__':
    main()
