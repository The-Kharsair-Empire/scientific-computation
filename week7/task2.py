def RK2(f, b, h, y0, x0, xMax, stepSize):
    a = 1-b
    alpha = (1/2)/b
    beta = (1/2)/b
    x = [x0]
    y = [y0]
    while x[-1]+ h < xMax:
        yi = y[-1]
        xi = x[-1]
        k1 = f(xi, yi)
        k2 = f(xi+alpha*h, yi+beta*h*k1)
        yip1 = yi + h*(a*k1 + b*k2)
        y.append(yip1)
        x.append(xi+h)

    return x, y

