from matplotlib.pyplot import plot, show


def cobwebbing(N0 = 1, para0 = 1.3, para1 = 0.1, tol = 1e-10, maxIter = 10):

    N = [N0]
    X = [0, N0]
    i = 0
    x = []
    y = []
    while i < maxIter:
        next = (para0 * N[-1]) / ((1 + N[-1]) ** para1)
        curY = (para0 * i) / ((1 + i) ** para1)
        y.append(curY)
        x.append(i)

        N += [next]
        if abs(N[-1]-X[-1]) < tol:
            print('here')
            return X, N, x, y
        N += [next]
        X += [next, next]
        i += 1

    N += [(para0 * N[-1]) / ((1 + N[-1]) ** para1)]

    return X, N, x, y



x, y, x1, y1 = cobwebbing()

# plot(x, y)
# show()
# plot(x, x)
# show()
# plot(x1, y1)
# show()
plot(x, y, 'r', x, x, 'b', x1, y1, 'g')
show()

