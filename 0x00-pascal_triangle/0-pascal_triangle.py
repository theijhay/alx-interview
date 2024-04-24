#!/usr/bin/python3
"""Pascal's Triangle"""
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle up to the n-th row.
    Returns an empty list if n <= 0.
    """
    if n <= 0:  # 4. Conditional Statements
        return []

    triangle = [[1]]  # 1. Lists and List Comprehensions

    for i in range(1, n):  # 3. Loops
        # Generate the next row using list comprehension
        prev_row = triangle[i - 1]
        current_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(i - 1)] + [1]  # 1. List Comprehensions, 6. Arithmetic Operations, 7. Indexing and Slicing
        triangle.append(current_row)  # 1. Lists

    return triangle  # 2. Functions
