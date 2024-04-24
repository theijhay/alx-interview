#!/usr/bin/python3

"""Pascal Triangle"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows in the Pascal's Triangle.

    Returns:
        list of lists: Pascal's Triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Start the row with 1
        prev_row = triangle[-1]  # Access the previous row

        for j in range(1, i):
            # Calculate each element using the previous row
            element = prev_row[j - 1] + prev_row[j]
            row.append(element)

        row.append(1)  # End the row with 1
        triangle.append(row)  # Append the row to the triangle

    return triangle
