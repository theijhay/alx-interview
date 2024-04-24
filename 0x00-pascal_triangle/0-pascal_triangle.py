#!/usr/bin/python3

"""Pascal Triangle"""

def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle up to n rows.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []  # If n is less than or equal to 0, return an empty list

    pascal = [0] * n  # Create a list of 0s with length n

    for i in range(n):
        # Create a new row with i+1 elements, all initialized to 0
        nrow = [0] * (i+1)

        # Set the first and last elements of the row to 1
        nrow[0] = 1
        nrow[len(nrow) - 1] = 1

        # Calculate the values for the middle elements of the row
        for j in range(1, i):
            if j > 0 and j < len(nrow):
                # Get the values from the previous row
                a = pascal[i - 1][j]
                b = pascal[i - 1][j - 1]

                # Calculate the value for the current element
                nrow[j] = a + b

        # Store the new row in the pascal list
        pascal[i] = nrow

    return pascal
