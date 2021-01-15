def poly_newton(arr, x0 = -1, tol = 1e-9):
    func = 0
    deri = 0
    x = x0
    xNext = x
    maxIter = 0
    while maxIter < 1000:
        for i in range(len(arr)):
            func += arr[i] * x ** (len(arr)-(i+1))

        for j in range(len(arr)-1):
            deri += arr[j]*(len(arr)-(j+1)) * x ** (len(arr)-(j+2))

        xNext = x - func/deri

        if abs((xNext-x)/x)*100 < tol:
            return xNext

        x = xNext

        func = 0
        deri = 0

    maxIter += 1


print(poly_newton([2, 0, 1, 1]))