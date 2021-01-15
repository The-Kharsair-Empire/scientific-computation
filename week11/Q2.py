import numpy as np
import math
import copy as cp
import random

# input = [
#     [[['@', 2, 4], [6, '@', '@'], ['@', '@', 3]], [['@', '@', 7], ['@', '@', '@'], [6, 8, '@']], [['@', '@', '@'], ['@', '@', '@'], [4, 1, 5]]],
#     [[[4, 3, 1], [5, '@', '@'], [7, 9, '@']], [['@', '@', 5], ['@', '@', '@'], ['@', '@', '@']], [['@', '@', '@'], ['@', 3, 2], ['@', 6, '@']]],
#     [[[2, '@', 9], ['@', 4, '@'], [3, 1, '@']], [[7, 1, '@'], ['@', 9, 3], ['@', '@', 4]], [[8, '@', '@'], ['@', '@', '@'], [7, 5, '@']]]
# ]

# input = [
#     [0, 4, 2, 0],
#     [2, 0, 0, 3],
#     [1, 0, 0, 4],
#     [0, 3, 1, 0]
# ]
# input = [
#     [0, 3, 0, 0],
#     [0, 0, 0, 0],
#     [0, 2, 0, 1],
#     [0, 1, 2, 0]
# ]

# input = [
#     [1, 0, 4, 9, 0, 6, 0, 0, 0],
#     [9, 2, 5, 0, 7, 4, 3, 6, 1],
#     [6, 7, 3, 5, 1, 2, 9, 8, 4],
#     [2, 0, 0, 0, 0, 0, 0, 1, 0],
#     [5, 0, 0, 4, 0, 8, 0, 9, 0],
#     [7, 9, 8, 0, 5, 1, 2, 4, 0],
#     [0, 0, 0, 7, 6, 0, 4, 2, 8],
#     [4, 6, 2, 1, 8, 3, 0, 5, 9],
#     [8, 5, 0, 2, 4, 0, 1, 0, 6]
# ]

input = [
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 9, 0, 3, 0, 7, 0, 4, 0],
    [6, 1, 0, 0, 8, 0, 0, 0, 3],
    [0, 0, 1, 2, 0, 0, 4, 0, 8],
    [0, 0, 6, 0, 0, 0, 0, 5, 0],
    [0, 4, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 4, 3, 0, 0],
    [4, 5, 0, 1, 0, 0, 0, 0, 2]
]
symbol = 0

reference = cp.deepcopy(input)

def fill(row):
    tempFill = [0 for _ in range(len(row) + 1)]
    for each in row:
        tempFill[each] += 1
    tempFill = list(zip(tempFill, list(range(len(row) + 1))))
    tempFill = tempFill[1:]
    tempFill = list(filter(lambda x: x[0] == 0, tempFill))
    tempFill = list(map(lambda x: x[1], tempFill))

    for i in range(len(row)):
        if row[i] == symbol:
            row[i] = np.random.choice(tempFill)
            break

def perturb(row, referencerow):

    temp = list(zip(referencerow, list(range(len(referencerow)))))
    temp = list(filter(lambda x: x[0] == 0, temp))
    temp = list(map(lambda x:x[1], temp))

    i, j = np.random.choice(len(temp), 2, replace=False)
    i, j = temp[i], temp[j]

    row[i], row[j] = row[j], row[i]


def cost(puzzle):
    retVal = 0
    n2 = len(puzzle)
    n = round(math.sqrt(n2))
    for i in range(n2):
        check = [-1 for _ in range(n2 + 1)]
        check[0] = 0
        for j in range(n2):
            check[puzzle[j][i]] += 1


        check = list(map(lambda x: 0 if x == -1 else x, check))
        retVal += sum(check)

    for i in range(0, n2, n):
        for j in range(0, n2, n):
            check = [-1 for _ in range(n2 + 1)]
            check[0] = 0
            for k in range(n):
                for p in range(n):
                    check[puzzle[i+k][j+p]] += 1

            check = list(map(lambda x: 0 if x == -1 else x, check))
            retVal += sum(check)

    return retVal


def SA(input, reference):
    for i in input:
        for j in range(len(input[0])):
            if symbol in i:
                fill(i)
    matrix = input
    cur_cost = cost(cp.deepcopy(input))
    while cur_cost > 0:
        a_row = np.random.choice(len(input))
        # while len(list(filter (lambda x:x==0, matrix[a_row]))) == 1:
        #     a_row = np.random.choice(len(input))
        new_matrix = cp.deepcopy(matrix)
        perturb(new_matrix[a_row], reference[a_row])

        pertubed_cost = cost(new_matrix)
        delta = pertubed_cost - cur_cost

        if delta < 0:
            matrix = new_matrix
            cur_cost = pertubed_cost
        elif np.random.random() < np.exp(-(delta / cur_cost)):
            matrix = new_matrix
            cur_cost = pertubed_cost
        # t = c_fac * t
    return matrix


# def crossover(submatrix1, submatrix2):
#     m1 = cp.deepcopy(submatrix1)
#     m2 = cp.deepcopy(submatrix2)
#
#
print(np.array(SA(input, reference)))
#
# def GA(N, generations, mutation_prob, crossover_prob, mutation = perturb):
#     pop_size = 5
#     parents = []
#     for i in range(pop_size):
#         chessBoard = [i for i in range(N)]
#         chessBoard = np.random.permutation(chessBoard)
#         parents.append(chessBoard)
#         # print('initial chessBoard: ', chessBoard)
#     costVal = np.array([cost(each) for each in parents])
#     fitness = 1.0/costVal
#     fp = fitness/(np.sum(fitness))
#     while generations > 0 and costVal.argmin() > 0:
#         children = []
#         fittest = parents[fitness.argmax()]
#         children.append(np.copy(fittest))
#         for _ in range(pop_size-1):
#             parent_index = np.random.choice(range(pop_size), p=fp)
#             parent = parents[parent_index]
#             if np.random.random() < mutation_prob:
#                 mutant = mutation(np.copy(parent))
#                 children.append(mutant)
#             elif np.random.random() < crossover_prob:
#                 another_parent_index = np.random.choice(range(pop_size), p=fp)
#                 another_parent = parents[another_parent_index]
#                 children.append(crossover(parent, another_parent))
#             else:
#                 children.append(np.copy(parent))
#
#         parents = children
#         costVal = np.array([cost(each) for each in parents])
#         fitness = 1.0 / costVal
#         fp = fitness / (np.sum(fitness))
#         generations -= 1
#     best = parents[costVal.argmin()]
#     return best