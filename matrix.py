def transpose(matrix):
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]

def powers(input_list, lower_limit, upper_limit):
    return [[i**j for j in range(lower_limit, upper_limit+1)] for i in input_list]
