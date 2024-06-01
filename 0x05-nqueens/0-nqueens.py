#!/usr/bin/python3
"""A program that solves the N queens problem."""

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if number < 4:
        print('N must be at least 4')
        exit(1)

    # initialization
    ls = []
    placedqueens = []
    stop = False
    row = 0
    column = 0

    # pass throug rows
    while row < number:
        goback = False
        # pass through columns
        while column < number:
            # check if safe to place queen
            safe = True
            for cord in placedqueens:
                col = cord[1]
                if (col == column or col + (row-cord[0]) == column or
                        col - (row-cord[0]) == column):
                    safe = False
                    break

            if not safe:
                if column == number - 1:
                    goback = True
                    break
                column += 1
                continue

            # this row is safe to place queen
            cords = [row, column]
            placedqueens.append(cords)
            """if last row is reached, add solution to list"""
            if row == number - 1:
                ls.append(placedqueens[:])
                for cord in placedqueens:
                    if cord[1] < number - 1:
                        row = cord[0]
                        column = cord[1]
                for i in range(number - row):
                    placedqueens.pop()
                if row == number - 1 and column == number - 1:
                    placedqueens = []
                    stop = True
                row -= 1
                column += 1
            else:
                column = 0
            break
        if stop:
            break
        """if no safe column found, go back to previous row and column"""
        if goback:
            row -= 1
            while row >= 0:
                column = placedqueens[row][1] + 1
                del placedqueens[row]
                if column < number:
                    break
                row -= 1
            if row < 0:
                break
            continue
        row += 1

    for index, value in enumerate(ls):
        if index == len(ls) - 1:
            print(value, end='')
        else:
            print(value)
