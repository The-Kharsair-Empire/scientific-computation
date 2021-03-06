from copy import deepcopy as cp
import numpy as np

A = [[25, 5, 1], [64, 8, 1], [144, 12, 1]]
b = [106.8, 177.2, 279.2]
def forward_sub(L, b):
    y = []
    for j in range(len(L)):
        if L[j][j] == 0:
            return 'no solution'
        y.append(b[j]/L[j][j])
        for i in range(j+1, len(L)):
            b[i] -= L[i][j] * y[j]

    return y

def back_sub(U, y):
    x = [0] * len(U)
    for j in range(len(U) - 1, -1, -1):
        if U[j][j] == 0:
            return "no solution"
        x[j] = y[j] / U[j][j]
        for i in range(0, j):
            y[i] = y[i] - (U[i][j] * x[j])
    return x

def LUdecomposition(A, b):
    I = [[1 if i == j else 0 for i in range(len(A[0]))] for j in range(len(A))]
    L = []
    Per = []

    for j in range(len(A[0])-1):
        M = cp(I)
        E = cp(I)
        P = cp(I)
        curM = A[j][j]
        maxI = j
        for k in range(j+1, len(A)):
            if abs(A[k][j]) > abs(curM):
                curM = A[k][j]
                maxI = k
        P[maxI], P[j] = P[j], P[maxI]
        # print(P)
        A = np.matmul(P, A)
        Per = cp(P) if Per == [] else np.matmul(P, Per)
        P = np.transpose(P)

        for i in range(j+1, len(A)):
            M[i][j] = (A[i][j]/A[j][j])*(-1)
            E[i][j] = (A[i][j]/A[j][j])
        A = np.matmul(M, A)
        L = cp(P) if L == [] else np.matmul(L, P)
        L = cp(E) if L == [] else np.matmul(L, E)



    L = np.matmul(Per, L)
    b = np.matmul(Per, b)

    # print('p: ', Per)
    # print('L: ', L)
    # print('U: ', A)


    return back_sub(A, forward_sub(L, b))

print('the result is: ', LUdecomposition(A, b))