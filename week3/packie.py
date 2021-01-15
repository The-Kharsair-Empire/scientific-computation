import numpy as np
from copy import deepcopy as cp
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
    for j in range(len(A[0])-1):
        M = cp(I)
        E = cp(I)
        for i in range(j+1, len(A)):
            M[i][j] = (A[i][j]/A[j][j])*(-1)
            E[i][j] = (A[i][j]/A[j][j])
        A = np.matmul(M, A)
        L = cp(E) if L == [] else np.matmul(L, E)


    return back_sub(A, forward_sub(L, b))


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