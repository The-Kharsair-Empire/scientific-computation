import scipy.linalg as la
import numpy as np
from matplotlib.pyplot import *

markovChain = np.array([
    [0, 1/3, 0, 0, 1/3, 0, 0, 0, 0, 1/3],
    [1/5, 0, 1/5, 0, 1/5, 0, 0, 0, 1/5, 1/5],
    [0, 0, 0, 0, 0, 1/2, 0, 0, 1/2, 0],
    [1/2, 0, 0, 0, 1/2, 0, 0, 0, 0, 0],
    [1/4, 1/4, 0, 1/4, 0, 0, 0, 0, 0, 1/4],
    [0, 0, 0, 0, 1/4, 0, 1/4, 1/4, 1/4, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1/3, 0, 0, 0, 0, 1/3, 0, 0, 1/3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1/3, 1/3, 0, 0, 0, 0, 0, 0, 1/3, 0]
])



# rank = list(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], eigval[1][0]))
# rank = sorted(rank, key=lambda x:x[1], reverse=True)
# rank = list(map(lambda x:x[0], rank))
# print(rank)
from random import *
def trajectory(markovChain):
    sample = []
    start = 0
    order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(10000):
        next = list(filter(lambda x: x[1]!=0, zip(order, markovChain[start])))
        ln = len(next)
        rd = randint(0, ln-1)
        nextstate = next[rd][0]
        sample.append(nextstate)
        start = nextstate

    return sample

def trajectory2(transition, markov):
    p = randint(1, 10)
    sample = []
    start = 0
    order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(10000):
        if p == 1:
            next = list(filter(lambda x: x[1] == 0, zip(order, markov[start])))
            ln = len(next)
            rd = randint(0, ln - 1)
            nextstate = next[rd][0]
            sample.append(nextstate)
            start = nextstate
        else:
            next = list(filter(lambda x: x[1]!=0, zip(order, markov[start])))
            ln = len(next)
            rd = randint(0, ln - 1)
            nextstate = next[rd][0]
            sample.append(nextstate)
            start = nextstate

    return sample

def analysis1(markovChain):
    eigval, eigvec = la.eig(markovChain, left=True, right=False)
    print(eigval[0], eigvec[0])
    print(eigvec[:, 0]/sum(eigvec[:,0]))
    # plot(range(10), np.real(eigvec[:, 0]/sum(eigvec[:,0])))
    transition = np.linalg.matrix_power(markovChain, 1000000)
    show()

    sd = np.matmul(np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), transition)
    # print(sd)


    rank = list(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], sd))
    rank = sorted(rank, key=lambda x:x[1], reverse=True)
    rank = list(map(lambda x:x[0], rank))
    # print(rank)

    hist(trajectory(markovChain), bins=[i-0.5 for i in range(11)])
    show()

analysis1(markovChain)



# def analysis2(Transition_new ,markovChain):
#     eigval, eigvec = la.eig(Transition_new, left=True, right=False)
#     print(eigvec[:, 0]/sum(eigvec[:,0]))
#     plot(range(10), np.real(eigvec[:, 0]/sum(eigvec[:,0])))
#     transition = np.linalg.matrix_power(Transition_new, 1000000)
#     show()
#
#     sd = np.matmul(np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), transition)
#     print(sd)
#
#
#     rank = list(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], sd))
#     rank = sorted(rank, key=lambda x:x[1], reverse=True)
#     rank = list(map(lambda x:x[0], rank))
#     print(rank)
#     temp = trajectory2(Transition_new ,markovChain)
#     # print(temp)
#     hist(temp, bins=[i-0.5 for i in range(11)])
#     show()

#partC
Transition_new = np.array([
    [1/7*0.1, 1/3*0.9, 1/7*0.1, 1/7*0.1, 1/3*0.9, 1/7*0.1, 1/7*0.1, 1/7*0.1, 1/7*0.1, 1/3*0.9],
    [1/5*0.9, 1/5*0.1, 1/5*0.9, 1/5*0.1, 1/5*0.9, 1/5*0.1, 1/5*0.1, 1/5*0.1, 1/5*0.9, 1/5*0.9],
    [1/8*0.1, 1/8*0.1, 1/8*0.1, 1/8*0.1, 1/8*0.1, 1/2*0.9, 1/8*0.1, 1/8*0.1, 1/2*0.9, 1/8*0.1],
    [1/2*0.9, 1/8*0.1, 1/8*0.1, 1/8*0.1, 1/2*0.9, 1/8*0.1, 1/8*0.1, 1/8*0.1, 1/8*0.1, 1/8*0.1],
    [1/4*0.9, 1/4*0.9, 1/6*0.1, 1/4*0.9, 1/6*0.1, 1/6*0.1, 1/6*0.1, 1/6*0.1, 1/6*0.1, 1/4*0.9],
    [1/6*0.1, 1/6*0.1, 1/6*0.1, 1/6*0.1, 1/4*0.9, 1/6*0.1, 1/4*0.9, 1/4*0.9, 1/4*0.9, 1/6*0.1],
    [1/9*0.1, 1/9*0.1, 1.*0.9, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1],
    [1/3*0.9, 1/7*0.1, 1/7*0.1, 1/7*0.1, 1/3*0.9, 1/7*0.1, 1/7*0.1, 1/3*0.9, 1/7*0.1, 1/7*0.1],
    [1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1/9*0.1, 1.*0.9],
    [1/3*0.9, 1/3*0.9, 1/7*0.1, 1/7*0.1, 1/7*0.1, 1/7*0.1, 1/7*0.1, 1/7*0.1, 1/3*0.9, 1/7*0.1]], dtype=float)


# analysis2(Transition_new, markovChain)