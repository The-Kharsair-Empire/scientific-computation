from matplotlib.pyplot import plot, show, title
def growth(para, N0):
    N = [N0]
    x = list(range(1, 100))
    for _ in x:
        next = (para[0]*N[-1])/((1+N[-1])**para[1])
        N.append(next)

    return [0]+x, N

init = 1
for i in [[1.3, 0.1], [10.6, 1.9], [75, 3.4]]:
    x, y = growth(i, init)
    plot(x, y)
    title(i)
    show()