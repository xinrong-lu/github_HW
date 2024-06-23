def matrix_multiplication(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        matrix = matrix_multiplication(n - 1)
        last_row = matrix[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        matrix.append(new_row)
        return matrix

def print_matrix_multiplication(matrix U, matrix V):
    max_width = max(len(str(num)) for row in matrix for num in row)
    if matrix_V == "normal":
        for row in matrix:
            row_str = " ".join(str(num) for num in row)
            print(row_str.center(len(matrix[-1]) * (max_width + 1)))
    elif matrix_V == "reverse":
        for row in reversed(matrix):
            row_str = " ".join(str(num) for num in row)
            print(row_str.center(len(matrix[-1]) * (max_width + 1)))
    elif matrix_V == "left":
        for row in matrix:
            row_str = " ".join(str(num) for num in row)
            print(row_str)
    elif matrix_V == "right":
        for row in matrix:
            row_str = " ".join(str(num) for num in row)
            print(row_str.rjust(len(matrix[-1]) * (max_width + 1)))

# Prompt the user for the number of rows
while True:
    try:
        num_rows = int(input("Enter matrix U: "))
        if num_rows < 1:
            print("Invalid input. Please enter an integer greater than or equal to 1.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Prompt the user for the matrix_V
while True:
    matrix_V = input("Enter matrix V: ").lower()
    if matrix_V < 1:
            print("Invalid input. Please enter an integer greater than or equal to 1.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Generate matrix_multiplication
matrix_U = matrix_multiplication(num_rows)

# Print matrix_multiplication according to the specified matrix_U
print("matrix_multiplication:")
print_pascal_triangle(matrix_U, matrix_V)
