def transpose(matrix):
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]
