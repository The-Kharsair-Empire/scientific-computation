#columns correspond to x, y, a, b, c, d, e, f, g, z, c
#for RHS_vec, last row will be the c for the obj_vec
import numpy as np
def simplexMethod(obj_vec, RHS_vec, coef_matrix):
    cur_best = 0
    decision_variable = [0 for i in range(len(obj_vec))]

    while True:
        if min(obj_vec) >= 0:
            break


        decision_variable = [0 for i in range(len(obj_vec))]

        largest_neg = 0
        largest_neg_index = 0
        for i in range(len(obj_vec)):
            if obj_vec[i] < largest_neg:
                largest_neg = obj_vec[i]
                largest_neg_index = i


        pivot = 0
        min_fraction = RHS_vec[0]/coef_matrix[0][largest_neg_index]
        for j in range(1, len(coef_matrix)):
            if coef_matrix[j][largest_neg_index] > 0:
                temp = RHS_vec[j]/coef_matrix[j][largest_neg_index]
            if temp < min_fraction:
                min_fraction = temp
                pivot = j


        base = coef_matrix[pivot][largest_neg_index]
        for k in range(len(coef_matrix[pivot])):
            coef_matrix[pivot][k] = coef_matrix[pivot][k]/base

        RHS_vec[pivot] = RHS_vec[pivot]/base

        for p in range(0, pivot):
            elimination_coef = -coef_matrix[p][largest_neg_index]
            for e in range(len(coef_matrix[p])):
                coef_matrix[p][e] = coef_matrix[p][e] + elimination_coef * coef_matrix[pivot][e]

            RHS_vec[p] = RHS_vec[p] + elimination_coef * RHS_vec[pivot]

        for q in range(pivot+1, len(coef_matrix)):
            elimination_coef = -coef_matrix[q][largest_neg_index]
            for e in range(len(coef_matrix[q])):
                coef_matrix[q][e] = coef_matrix[q][e] + elimination_coef * coef_matrix[pivot][e]

            RHS_vec[q] = RHS_vec[q] + elimination_coef * RHS_vec[pivot]

        elimination_coef = -obj_vec[largest_neg_index]
        for e in range(len(obj_vec)):
            obj_vec[e] = obj_vec[e] + elimination_coef * coef_matrix[pivot][e]

        RHS_vec[-1] = RHS_vec[-1] + elimination_coef * RHS_vec[pivot]

        for i in range(len(obj_vec)):
            if obj_vec[i] == 0:
                for j in range(len(coef_matrix)):
                    if coef_matrix[j][i] == 1:
                        decision_variable[i] = round(RHS_vec[j])

        cur_best = round(RHS_vec[-1])
    # print(RHS_vec)
    # print(np.array(coef_matrix))
    # print(obj_vec)


    return cur_best, decision_variable

obj_vec = [-1, -2, 0, 0, 0, 0, 0, 0, 0, 1]
RHS_vec = [44, 39, 37, 9, 6, 0, 0, 0]
coef_matrix = [
    [4, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [3, 2, 0, 1, 0, 0, 0, 0, 0, 0],
    [2, 3, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [-1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 1, 0]
]

maximum, objective_vector = simplexMethod(obj_vec, RHS_vec, coef_matrix)

print(maximum)
print(objective_vector)

o = [-6, -5, 0, 0, 0, 0, 1]
r = [5, 12, 0, 0, 0]
c = [
    [1, 1, 1, 0, 0, 0, 0],
    [3, 2, 0, 1, 0, 0, 0],
    [-1, 0, 0, 0, 1, 0, 0],
    [0, -1, 0, 0, 0, 1, 0]
]

m, ov = simplexMethod(o, r, c)
print(m)
print(ov)




