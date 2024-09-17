def transpose(matrix):
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]


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