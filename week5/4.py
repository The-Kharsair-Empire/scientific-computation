from math import log,exp
from matplotlib.pyplot import plot, show, title
def growth(r, K, N0):
    N = [N0]
    x = list(range(1, 100))
    for _ in x:
        next = N[-1] + N[-1]*r*(1-N[-1]/K)
        N.append(next)

    return [0]+x, N

for n0 in [100, 101, 99]:
    for r in [0.5, 2.3, 3]:
        x, y = growth(r, 1000, n0)
        plot(x, y)
        t = 'r = ' + str(r) + '  ' + 'n0 = ' + str(n0)
        title(t)
        show()

