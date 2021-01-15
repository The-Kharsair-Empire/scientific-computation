from math import log,exp
from matplotlib.pyplot import plot, show
def growth(a, K, N0):
    N = [N0]

    x = list(range(1, 100))
    for _ in x:
        next = N[-1]*exp(a*(1-N[-1]/K))
        N.append(next)

    return [0]+x, N

x, y = growth(5, 1000, 100)
print(len(x), len(y))
plot(x, y)
show()


