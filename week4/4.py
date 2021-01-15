import math
from scipy import optimize as op

def newton(func, x0 = 1, tol = 1e-9, max_iter = 1000):
    def derivative(x):
        run = 1./1000.
        rise = func(x + run) - func(x)
        return rise/run
    x = x0
    for _ in range(max_iter):
        xNext = x - func(x)/derivative(x)
        if abs((xNext-x)/x)*100 < tol:
            return xNext
        x = xNext

    return 'can''t find answer!'


def func1(x):
    return x ** 3 - 2 * x - 5

print('calculated by my newton: ', newton(func1))
print('calculated using scipy : ', op.newton(func1, 1))

def func2(x):
    return math.exp(-x) - x

print('calculated by my newton: ', newton(func2))
print('calculated using scipy : ', op.newton(func2, 1))

def func3(x):
    return x * math.sin(x) - 1

print('calculated by my newton: ', newton(func3, ))
print('calculated using scipy : ', op.newton(func3, 1))

def func4(x):
    return x ** 3 - 3 * x ** 2 + 3 * x - 1

print('calculated by my newton: ', newton(func4, ))
print('calculated using scipy : ', op.newton(func4, 1))


def secant(func, x0, x1, tol = 1e-9, max_iter = 1000):
    i, j = x1, x0
    for _ in range(max_iter):
        xNext = i - func(i)*(i-j)/(func(i) - func(j))
        if abs((xNext - i)/i) < tol:
            return xNext
        j = i
        i = xNext

    return 'can''t find answer'


print('calculated by my secant: ', secant(func1, 1, 2))
print('calculated by my secant: ', secant(func2, 1, 2))
print('calculated by my secant: ', secant(func3, 1, 2))
print('calculated by my secant: ', secant(func4, 1, 2))

