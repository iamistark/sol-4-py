def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
#Driver code
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))
