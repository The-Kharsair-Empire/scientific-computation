def euler(f, b, h, y0, x0, xMax, stepSize):
    x = [x0]
    y = [y0]
    while x[-1]+h < xMax:
        xi = x[-1]
        yi = y[-1]
        yip1 = yi + h * f(xi, yi)
        x.append(xi+h)
        y.append(yip1)
    return x, y


