def transpose(matrix):
    if len(matrix) == 0:
        return []
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]

def powers(input_list, lower_limit, upper_limit):
    return [[i**j for j in range(lower_limit, upper_limit+1)] for i in input_list]

def loadtxt(file_path):
    with open(file_path) as file:
        return [[float(value.rstrip("\n")) for value in line.split("\t")] for line in file]

def matmul(matrixa, matrixb):
    if len(matrixa) == 0 or len(matrixb) == 0:
        return []
    output=[]
    first_matrix, second_matrix = matrixb, matrixa
    if len(matrixa[0]) == len(matrixb):
        first_matrix, second_matrix = matrixa, matrixb

    for row_id,alist in enumerate(first_matrix):
        output.append([])
        for i,itema in enumerate(alist):
            for column_id, itemb in enumerate(second_matrix[i]):
                if i == 0:
                    output[row_id].append(0)
                output[row_id][column_id]+=itema*itemb

    return output

def invert(matrix):
    det = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    output=[[0,0],[0,0]]
    for i, li in enumerate(matrix):
        for n, item in enumerate(li):
            if n!=i:
                item = item*-1
            item=item/det
            if i==0:
                output[n-1][1]=item
            else:
                output[n-1][0]=item
   
    return output
