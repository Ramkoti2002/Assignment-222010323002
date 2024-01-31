def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for row_num in range(1, numRows):
        previous_row = triangle[row_num - 1]
        current_row = [1]  # First element of each row is always 1

        for col_num in range(1, row_num):
            # Calculate the element by summing up elements from the previous row
            current_row.append(previous_row[col_num - 1] + previous_row[col_num])

        current_row.append(1)  # Last element of each row is always 1
        triangle.append(current_row)

    return triangle

# Example usage:
numRows = 5
result = generate_pascals_triangle(numRows)
print(result)

