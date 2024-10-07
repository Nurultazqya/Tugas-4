def multiply_matrices(A, B):
    if len(A[0]) != len(B):
       return "Matriks tidak dapat dikalikan"

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))] 

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result 

# contoh penggunaan
A = [[1,2,4],[3,5,6],[7,2,9]]
B = [[3,8,5],[3,5,4],[3,6,1]]
print(multiply_matrices(A, B))