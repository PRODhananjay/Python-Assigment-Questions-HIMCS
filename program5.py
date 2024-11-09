# Find Transpose of a Matrix

A = [[1, 3, 4],
     [4, 8, 9],
     [4, 7, 5]]

# Initialize the result matrix with 0s
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Transpose the matrix
for i in range(len(A)):
    for j in range(len(A[0])):
        result[j][i] = A[i][j]

print("The transpose of the matrix is:")
for r in result:
    print(r)
