import numpy as np
from q1 import *
from matplotlib.pyplot import *
def the_func(x):
    return np.sqrt(2/np.pi)*np.exp(-x**2/2)


def p(x, c = 1, lambda_=1):
    return (lambda_*np.exp(-lambda_*x))*c

x = [i*0.01 for i in range(500)]
y = [the_func(i) for i in x]
plot(x, y, label='f(x)')

c = max([the_func(i)/p(i) for i in x])

y = [p(i, c) for i in x]
plot(x, y, label='c x p(x)')
legend()
grid()
show()

def rej_sam():
    while True:
        X = -np.log(np.random.random())
        u = np.random.random()
        if u < the_func(X)/p(X, c):
            return X


result = []
for i in range(200000):
    result.append(rej_sam())

hist(result)
show()