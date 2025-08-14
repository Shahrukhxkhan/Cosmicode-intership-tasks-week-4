def matrix_multiply(A, B):
    return [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

# Get dimensions for first matrix
rows_A = int(input("Enter number of rows for matrix A: "))
cols_A = int(input("Enter number of columns for matrix A: "))

# Get first matrix
print("Enter elements for matrix A (row-wise, space-separated):")
A = []
for i in range(rows_A):
    row = list(map(int, input().split()))
    A.append(row)

# Get dimensions for second matrix
rows_B = int(input("Enter number of rows for matrix B: "))
cols_B = int(input("Enter number of columns for matrix B: "))

# Check if multiplication is possible
if cols_A != rows_B:
    print("Matrix multiplication not possible!")
else:
    # Get second matrix
    print("Enter elements for matrix B (row-wise, space-separated):")
    B = []
    for i in range(rows_B):
        row = list(map(int, input().split()))
        B.append(row)
    
    # Perform multiplication
    result = matrix_multiply(A, B)
    
    # Display result
    print("Result of matrix multiplication:")
    for row in result:
        print(' '.join(map(str, row)))