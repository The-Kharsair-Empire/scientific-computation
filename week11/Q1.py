import numpy as np

def display(input):
    board = [[0 for _ in range(len(input))] for _ in range(len(input))]
    for i in range(len(input)):
        board[i][input[i]] = 1
    print(np.array(board))

def perturb(chessBoard):
    i, j = np.random.choice(len(chessBoard), 2, replace=False)
    new_chessBoard = np.copy(chessBoard)
    new_chessBoard[i], new_chessBoard[j] = new_chessBoard[j], new_chessBoard[i]
    return new_chessBoard

def cost(chessBoard):
    clash = 0
    for each in range(len(chessBoard)):
        for rest in range(each+1, len(chessBoard)):
            if chessBoard[rest] == chessBoard[each] + (rest-each) or chessBoard[rest] == chessBoard[each] - (rest-each):
                clash += 1
    return clash

def SA(N, coolingFactor):
    chessBoard = [i for i in range(N)]
    chessBoard = np.random.permutation(chessBoard)
    assert 0 < coolingFactor < 1
    t = cost(chessBoard)
    while t > 0:

        pertubed_chessBoard = perturb(chessBoard)
        pertubed_cost = cost(pertubed_chessBoard)
        delta = pertubed_cost - t

        if delta < 0:
            chessBoard = pertubed_chessBoard
            t = pertubed_cost
        elif np.random.random() < np.exp(-delta/t):
            chessBoard = pertubed_chessBoard
            t = pertubed_cost
    return chessBoard

sol = SA(10, 0.1)
display(sol)
print(sol)


def crossover(chessBoardA, chessBoardB):
    cutoff = np.random.randint(0, len(chessBoardA))
    retVal = []
    for i in range(cutoff):
        retVal.append(chessBoardA[i])
    i = 0
    while len(retVal) < len(chessBoardA):
        if chessBoardB[i] not in retVal:
            retVal.append(chessBoardB[i])
        i += 1
    return retVal

def GA(N, generations, mutation_prob, crossover_prob, mutation = perturb):
    pop_size = 100
    parents = []
    for i in range(pop_size):
        chessBoard = [i for i in range(N)]
        chessBoard = np.random.permutation(chessBoard)
        parents.append(chessBoard)
        # print('initial chessBoard: ', chessBoard)
    costVal = np.array([cost(each) for each in parents])
    fitness = 1.0/costVal
    fp = fitness/(np.sum(fitness))
    while generations > 0 and costVal.argmin() > 0:
        children = []
        fittest = parents[fitness.argmax()]
        children.append(np.copy(fittest))
        for _ in range(pop_size-1):
            parent_index = np.random.choice(range(pop_size), p=fp)
            parent = parents[parent_index]
            if np.random.random() < mutation_prob:
                mutant = mutation(np.copy(parent))
                children.append(mutant)
            elif np.random.random() < crossover_prob:
                another_parent_index = np.random.choice(range(pop_size), p=fp)
                another_parent = parents[another_parent_index]
                children.append(crossover(parent, another_parent))
            else:
                children.append(np.copy(parent))

        parents = children
        costVal = np.array([cost(each) for each in parents])
        fitness = 1.0 / costVal
        fp = fitness / (np.sum(fitness))
        generations -= 1
    best = parents[costVal.argmin()]
    return best

sol = GA(10, 1000, 0.1, 0.1)
display(sol)
print(sol)
