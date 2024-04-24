#!/usr/bin/python3
"""Pascal's Triangle"""
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows in the Pascal's Triangle.

    Returns:
        list of lists: Pascal's Triangle represented as a list of lists of integers.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row [1]
    triangle = [[1]]

    # Iterate to generate subsequent rows
    for i in range(1, n):
        # Create a new row list
        row = [1]
        # Access the previous row
        prev_row = triangle[i - 1]

        # Calculate the values for the current row based on the previous row
        for j in range(1, i):
            # Use addition to calculate each element
            element = prev_row[j - 1] + prev_row[j]
            # Append the calculated element to the current row
            row.append(element)

        # Append 1 at the end of the row
        row.append(1)
        # Append the generated row to the triangle
        triangle.append(row)

    # Return the completed Pascal's Triangle
    return triangle

# Test the pascal_triangle function with 5 rows
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    # Print the Pascal's Triangle with 5 rows
    print_triangle(pascal_triangle(5))
