matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose matrix
transpose_matrix = [
    [matrix[j][i] for j in range(len(matrix))] 
    for i in range(len(matrix[0]))  
]

for row in transpose_matrix:
    print(row)