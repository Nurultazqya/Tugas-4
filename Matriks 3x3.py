def multiply_matrices(A, B):
    if len(A[0]) != len(B):
      return "matriks tidak dapat dikalikan"

    result = [[0 for_in range(len(B[0]))]

    for_in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k]*B[k][j]

    retusrn result 
  
# contoh penggunaan
A = [[1,2,2],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
print(multiply_matrices(A, B))
