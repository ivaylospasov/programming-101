#!/usr/bin/env python3


def ABCheck(some_string):
    a_list = [x for x in range(len(some_string)) if some_string[x] == 'a']
    b_list = [y for y in range(len(some_string)) if some_string[y] == 'b']
    # A list with positive values of a's and b's indexes
    sbt_results = [abs(x - y) for x in a_list for y in b_list]
    # The number of places between a's and b's has to be 4
    if 4 in sbt_results:
        return True
    else:
        return False


def main():
    print(ABCheck('Laura sobs'))
    print(ABCheck('bfter abdly'))

if __name__ == '__main__':
    main()
