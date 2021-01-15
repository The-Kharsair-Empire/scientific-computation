from copy import deepcopy as cp
import numpy as np
b = [1, 3, 5]
A = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]

def back_sub(E, b):
    x = [0]*len(E)
    for j in range(len(E)-1, -1, -1):
        if E[j][j] == 0:
            return "no solution"
        x[j] = b[j]/E[j][j]
        # print(j)
        for i in range(0, j):
            # print('i', i)
            b[i] = b[i] - (E[i][j]*x[j])
    return x

def GassianElimination(A, b):
    I = [[1 if i == j else 0 for i in range(len(A[0]))] for j in range(len(A))]
    L = []
    for j in range(len(A[0])-1):
        M = cp(I)
        for i in range(j+1, len(A)):
            M[i][j] = (A[i][j]/A[j][j])*(-1)
        A = np.matmul(M, A)
        L = cp(M) if L == [] else np.matmul(M, L)

    b = np.matmul(L, b)

    return back_sub(A, b)

print('the result of gassian elimination is: ',GassianElimination(A, b))


a = [[25, 5, 1], [64, 8, 1], [144, 12, 1]]
# print(np.linalg.inv(a))
bi = [106.8, 177.2, 279.2]
p = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
u = [[144, 12, 1], [0, 8, 1], [0, 0, 1]]
ldash = np.linalg.inv(np.matmul(u, np.linalg.inv(a)))
l = np.matmul(p, ldash)
print(l)


