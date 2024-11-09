# Program to add two matrix

A = [[1,3,4],
     [4,8,9],
     [4,7,5]]
     
B = [[1,3,4],
     [4,8,9],
     [4,7,5]]
  
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print("The result of two matrix is :")
for r in result:
    print (r)