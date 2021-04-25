def transpose(matrix, n):
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
    print(matrix)
    
    
matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose(matrix, 3)


#time complexity is O(n^2)
#space complexity is O(1)
