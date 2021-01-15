from math import exp
from matplotlib.pyplot import plot, show, title
def growth(N0, P0, gamma = 0.068, c = 1, l = 2):
    N = [N0]
    P = [P0]

    x = list(range(1, 45))
    for _ in x:
        f = exp(-gamma * P[-1])
        nextN = l*f*N[-1]
        N.append(nextN)
        nextP = c*N[-1]*(1-f)
        P.append(nextP)

    return [0]+x, N, P

x, n, p = growth(50, 100)

plot(x, n, 'b')
title('host')
show()
plot(x, p, 'r')
title('parasite')
show()
plot(x, n, 'b', x, p, 'r')
show()


