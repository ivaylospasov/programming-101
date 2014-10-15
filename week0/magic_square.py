#!/usr/bin/env python3


def magic_square(matrix):
    matrix_sums_set = set()
    matrix_dimentions_digits = []
    first_diagonal = []
    second_diagonal = []
    transposed_matrix = [[row[i] for row in matrix]
                         for i in range(len(matrix))]
    for idx, row in enumerate(matrix):
        matrix_dimentions_digits.append(row)

    for idx, row in enumerate(transposed_matrix):
        matrix_dimentions_digits.append(row)

    for row in range(len(matrix)):
        first_diagonal.append(matrix[row][row])
        second_diagonal.append(matrix[row][(len(matrix) - 1) - row])
    matrix_dimentions_digits.append(first_diagonal)
    matrix_dimentions_digits.append(second_diagonal)

    for idx, list in enumerate(matrix_dimentions_digits):
        matrix_sums_set.add(sum(list))

    if len(matrix_sums_set) == 1:
        return True
    else:
        return False


def main():
    print(magic_square([[4, 9, 2],
                        [3, 5, 7],
                        [8, 1, 6]]))

if __name__ == '__main__':
    main()
