#!/usr/bin/env python3


def sum_matrix(m):
    x = []
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            x.append(m[i][j])
    for num in x:
        count += num
    return count

'''
# The easy way
def sum_matrix(m):
    count = 0
    x = sum(m, [])
    for i in x:
        count += i
    return count
'''


def main():
    print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

if __name__ == '__main__':
    main()
