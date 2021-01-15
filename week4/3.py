import math
import numpy as np
from scipy import optimize as op

def bisect(func, a, b, tol = 1e-5, max_iter = 1000):
    for _ in range(max_iter):
        mid = (a+b)/2
        if abs(a-b) < tol:
            return mid

        if func(a) > 0:
            if func(mid) > 0:
                a = mid
            else:
                b = mid
        elif func(b) >= 0:
            if func(mid) > 0:
                b = mid
            else:
                a = mid
    return "can't find root before iteration limit"


def func1(x):
    return x**3 - 2*x - 5

print('calculated by my bisect: ', bisect(func1, 0, 1000))
print('calculated using scipy : ', op.bisect(func1, 0, 1000))

def func2(x):
    return math.exp(-x) - x

print('calculated by my bisect: ', bisect(func2, 0, 1000))
print('calculated using scipy : ', op.bisect(func2, 0, 1000))

def func3(x):
    return x*math.sin(x) - 1

print('calculated by my bisect: ', bisect(func3, 0, 2))
print('calculated using scipy : ', op.bisect(func3, 0, 2))

def func4(x):
    return x**3 - 3*x**2 + 3*x - 1

print('calculated by my bisect: ', bisect(func4, 0, 1000))
print('calculated using scipy : ', op.bisect(func4, 0, 1000))
