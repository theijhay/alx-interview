#!/usr/bin/python3
"""Pascal Triangle"""

def pascal_triangle(n):
    """returns a pascal triangle of n rows"""
    
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0

    pascal = [0] * n  # Create a list of n zeros to represent the triangle

    for i in range(n):
        # Create a new row for each iteration
        nrow = [0] * (i + 1)  # Initialize the new row with zeros

        # Set the first and last element of the row to 1
        nrow[0] = 1
        nrow[-1] = 1

        # Calculate the elements in between using the previous row
        for j in range(1, i):
            if j > 0 and j < len(nrow):
                a = pascal[i - 1][j]  # Get the value from the previous row
                b = pascal[i - 1][j - 1]  # Get the value from the previous row and previous column
                nrow[j] = a + b  # Calculate the current element based on the values above

        pascal[i] = nrow  # Update the triangle with the new row

    return pascal  # Return the generated Pascal's Triangle
