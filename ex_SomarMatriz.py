# Autor: Lucas Toshio
# Data 05/06/23


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

print(C)        
