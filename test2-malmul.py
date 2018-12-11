A = [
    [1,2],
    [3,4],
    [5,6]
]
B = [
    [1,2,3],
    [4,5,6]
]

def find_row(mat,m):
    return mat[m]


def find_col(mat,n):
    row_num = len(mat)
    col = []
    for i in range(row_num):
        col.append(mat[i][n])
    return col

def vec_mul(row,col):
    result = 0
    for i in range(len(row)):
        result += row[i] * col[i]
    return result


def matmul(A,B):
    result = []
    for i in range(len(A)):
        tmp = []
        for j in range(len(B[0])):
            tmp.append(vec_mul(find_row(A,i),find_col(B,j)))
        result.append(tmp)
    return result

print(matmul(A,B))

