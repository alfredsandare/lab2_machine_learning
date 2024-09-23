def transpose(matrix):
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]

def powers(input_list, lower_limit, upper_limit):
    return [[i**j for j in range(lower_limit, upper_limit+1)] for i in input_list]

def loadtxt(file_path):
    with open(f"given_stuff/{file_path}") as file:
        return [[value.rstrip("\n") for value in line.split("\t")] for line in file]

def matmul(matrixa, matrixb):
    output=[]
    if len(matrixa[0])== len(matrixb):
        for n in range(len(matrixa)):
            output.append([])
            for i in range(len(matrixb[0])):
                output[n].append(0)

        for row_id,alist in enumerate(matrixa):
            for i,itema in enumerate(alist):
                for column_id, itemb in enumerate(matrixb[i]):
                    output[row_id][column_id]+=itema*itemb
    else:
        for n in range(len(matrixb)):
            output.append([])
            for i in range(len(matrixa[0])):
                output[n].append(0)

        for row_id,blist in enumerate(matrixb):
            for i,itemb in enumerate(blist):
                for column_id, itema in enumerate(matrixa[i]):
                    output[row_id][column_id]+=itema*itemb
                      
    return(output)

def invert(matrix):
    det = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    print(det)
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