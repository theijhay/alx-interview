#!/usr/bin/env python3
"""Pascal's Triangle"""
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle up to the n-th row.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        # Generate the next row using list comprehension
        prev_row = triangle[i - 1]
        current_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(i - 1)] + [1]
        triangle.append(current_row)

    return triangle
