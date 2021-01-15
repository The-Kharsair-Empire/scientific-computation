import numpy as np


def first(x):
    return np.sin(np.pi * x)

def second(x):
    return 1/(1+x)

def MonteCarlo(sample_num, func):
    under = 0

    for _  in range(sample_num):
        randPoint = np.random.random(2)
        if randPoint[1] < func(randPoint[0]):
            under += 1
    return under/sample_num


print(MonteCarlo(111000, first))
print(MonteCarlo(102932, second))

