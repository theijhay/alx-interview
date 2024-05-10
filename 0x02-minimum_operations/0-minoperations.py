#!/usr/bin/python3
"""minimum operations alx challenge"""


def minOperations(n):
    """minimum operations function"""
    chars = 1  # number of chars in the file
    board = 0  # number of H's copied
    counter = 0  # counter of operations

    while chars < n:
        # if no copy yet
        if board == 0:
            # copy all
            board = chars
            # increment operations counter by 1
            counter += 1

        # if no paste yet
        if chars == 1:
            # paste
            chars += board
            # increment operations counter by 1
            counter += 1
            # continue
            continue

        remaining = n - chars  # remaining chars to reach n
        # if remaining
        # is less than board
        # or can't be devided by board
        # then it's impossible to achieve n of chars
        # return 0
        if remaining < board:
            return 0

        # if remaining can be devided by board
        if remaining % chars != 0:
            # copyall
            chars += board
            # increment operations counter
            counter += 1
        else:
            # copy all
            board = chars
            # paste
            chars += board
            # increment operations counter by 2
            counter += 2

    # if chars is equal to n
    if chars == n:
        return counter
    else:
        return 0
