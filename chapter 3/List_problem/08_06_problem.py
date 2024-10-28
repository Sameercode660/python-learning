# Write a program to add 3 X 4 matrices

matrix1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4]]
matrix2 = [[2,3,4,5], [8,9,7,6], [5,7,9,3]]

matrix3 = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

for i in range(len(matrix1)):
    #iterate throught columns
    for j in range(len(matrix1[0])):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

for x in range(len(matrix3)):
    [print(value, end="\t") for value in matrix3[x]]
    print()