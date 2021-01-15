import numpy as np
#partA
def computeMatrix():

    matrix = [[0 for _ in range(62)] for _ in range(62)]

    snake = {25:11, 32:16, 48:34, 58:45}
    ladder = {3:17, 20:33, 28:42, 40:46, 47:60}
    for i in range(len(matrix)-1):

        for j in range(1, 7):
            temp = i + j
            if i+j > 61:
                temp = 61
            if temp+1 in snake:
                temp = snake[temp+1]-1
            if temp+1 in ladder:
                temp = ladder[temp+1]-1
            matrix[i][temp] += np.divide(1.0, 6.0)

    matrix = np.array(matrix)

    return matrix

def canonicalForm(matrix):
    # for i in matrix:
    #     for j in i:
            # print(j)
            # print(j == 1.0)
            # if j == 1.0:
            #     print(' is 1')
    matrix[[-1, -2]] = matrix[[-2, -1]]
    Q = matrix[:-1, :-1]
    R = matrix[:-1, -1]

    return Q, R


t = computeMatrix()
q, r = canonicalForm(t)
print('this is markov chain: ',t)
print('this is Q: ',q)
print('this is R: ',r)

#partB

def getN(Q):

    N = np.linalg.inv(np.subtract(np.identity(len(Q)), Q))
    return N


t = computeMatrix()
q, r = canonicalForm(t)
n = getN(q)
print('this is N: ',n)

maxt = 0
maxi = 0
maxj = 0
mint = 2
mini = 0
minj = 0
for i in range(len(n)):
    for j in range(len(n[0])):
        if n[i, j] > maxt:
            maxt = n[i, j]
            maxi = i
            maxj = j
        if n[i, j] < mint:
            mint = n[i, j]
            mini = i
            minj = j

print('most visited term N{a},{b}, times: {c}'.format(c=maxt, a=maxi+1, b=maxj+1))
print('least visited term N{},{}, times: {}'.format(mini+1, minj+1, mint))

#partC
from random import *
from matplotlib.pyplot import *
def abstime(N):
    ones = np.array([1 for i in range(len(N))])
    return np.matmul(N, ones)[0]

time = abstime(n)
print('time is: ', time)

def dice():
    p = randint(1, 6)
    return p

def game():
    played = 0
    state = 0                                                                                                   
    while state < 62:
        state += dice()
        played += 1
    return played

times = []
for i in range(1000):
    times.append(game())
hist(times, bins=range(min(times), max(times)+1))
print(sum(times)/len(times))

show()
#D
def moreDice(nOfDice):

    matrix = [[0 for _ in range(62)] for _ in range(62)]

    snake = {25:11, 32:16, 48:34, 58:45}
    ladder = {3:17, 20:33, 28:42, 40:46, 47:60}
    for i in range(len(matrix)-1):

        for j in range(1+(nOfDice-1), 6*nOfDice+1):
            temp = i + j
            if i+j > 61:
                temp = 61
            if temp+1 in snake:
                temp = snake[temp+1]-1
            if temp+1 in ladder:
                temp = ladder[temp+1]-1
            matrix[i][temp] += np.divide(1.0, 6.0*nOfDice)

    matrix = np.array(matrix)

    return matrix

times = []
x = list(range(1, 20))
for i in x:
    times.append(abstime(getN(canonicalForm(moreDice(i))[0])))

plot(x, times)

show()
