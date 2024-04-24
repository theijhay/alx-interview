#!/usr/bin/python3

"""Pascal Triangle"""

def pascal_triangle(n):
    """returns a pascal triangle of n rows"""
    if n <= 0:
        return []

    pascal = [0] * n

    for i in range(n):
        # include the first row
        nrow = [0] * (i+1)
        nrow[0] = 1
        nrow[len(nrow) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(nrow):
                a = pascal[i - 1][j]
                b = pascal[i - 1][j - 1]
                nrow[j] = a + b

        pascal[i] = nrow

    return pascal
