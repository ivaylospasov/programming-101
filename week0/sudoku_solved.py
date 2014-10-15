#!/usr/bin/env python3


def sudoku_grids(sudoku):
    small_grids = []
    coordintes = {1: [3, 6],
                  2: [6, 9]}
    square_one = [sudoku[row][column]
                  for row in range(coordintes[1][0])
                  for column in range(coordintes[1][0])]
    square_two = [sudoku[row][column]
                  for row in range(coordintes[1][0])
                  for column in range(coordintes[1][0], coordintes[1][1])]
    square_three = [sudoku[row][column]
                    for row in range(coordintes[1][0])
                    for column in range(coordintes[2][0], coordintes[2][1])]
    square_four = [sudoku[row][column]
                   for row in range(coordintes[1][0], coordintes[1][1])
                   for column in range(coordintes[1][0])]
    square_five = [sudoku[row][column]
                   for row in range(coordintes[1][0], coordintes[1][1])
                   for column in range(coordintes[1][0], coordintes[1][1])]
    square_six = [sudoku[row][column]
                  for row in range(coordintes[1][0], coordintes[1][1])
                  for column in range(coordintes[2][0], coordintes[2][1])]
    square_seven = [sudoku[row][column]
                    for row in range(coordintes[2][0], coordintes[2][1])
                    for column in range(coordintes[1][0])]
    square_eight = [sudoku[row][column]
                    for row in range(coordintes[2][0], coordintes[2][1])
                    for column in range(coordintes[1][0], coordintes[1][1])]
    square_nine = [sudoku[row][column]
                   for row in range(coordintes[2][0], coordintes[2][1])
                   for column in range(coordintes[2][0], coordintes[2][1])]
    small_grids.append(square_two)
    small_grids.append(square_one)
    small_grids.append(square_three)
    small_grids.append(square_four)
    small_grids.append(square_five)
    small_grids.append(square_six)
    small_grids.append(square_seven)
    small_grids.append(square_eight)
    small_grids.append(square_nine)
    return small_grids


def sudoku_solved(sudoku):
    set_one_to_nine = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    transposed_sudoku = [[row[i] for row in sudoku]
                         for i in range(len(sudoku))]
    for row in sudoku:
        if set(row) != set_one_to_nine:
            return False
    for row in transposed_sudoku:
        if set(row) != set_one_to_nine:
            return False
    for square in sudoku_grids(sudoku):
        if set(square) != set_one_to_nine:
            return False
    return True


def main():
    print(sudoku_solved([[4, 5, 2, 3, 8, 9, 7, 1, 6],
                         [3, 8, 7, 4, 6, 1, 2, 9, 5],
                         [6, 1, 9, 2, 5, 7, 3, 4, 8],
                         [9, 3, 5, 1, 2, 6, 8, 7, 4],
                         [7, 6, 4, 9, 3, 8, 5, 2, 1],
                         [1, 2, 8, 5, 7, 4, 6, 3, 9],
                         [5, 7, 1, 8, 9, 2, 4, 6, 3],
                         [8, 9, 6, 7, 4, 3, 1, 5, 2],
                         [2, 4, 3, 6, 1, 5, 9, 8, 7]
                         ]))

if __name__ == '__main__':
    main()
