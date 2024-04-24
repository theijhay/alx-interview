def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]  # Each row starts and ends with 1

        # Calculate the values for the current row
        for j in range(1, i):
            value = prev_row[j - 1] + prev_row[j]
            current_row.append(value)

        current_row.append(1)  # End the row with 1
        triangle.append(current_row)

    return triangle
