import numpy as np

print("rows and cols: ")
r,c = int(input()),int(input())
print("Enter values: ")
mat = np.zeros((r, c), int)
for i in range(r):
    for j in range(c):
        mat[i][j] = int(input())
print("Given matrix:\n", mat)
print("Sum of columns: ", mat.sum(axis = 0))
print("Sum of rows: ", mat.sum(axis = 1))