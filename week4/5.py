import math
from scipy import optimize as op
import matplotlib.pyplot as plt

def newton(func, derivative, x0 = 1, tol = 1e-9, max_iter = 1000):

    ansX = [x0]
    x = x0

    for _ in range(max_iter):
        xNext = x - func(x)/derivative(x)
        ansX.append(xNext)
        if abs((xNext-x)) < tol:
            return xNext, ansX
        x = xNext

    return 'can''t find answer!'

def func1(x):
    return x**2 - 1

def func1deri(x):
    return 2*x
ans = newton(func1, func1deri, 10**6)
print('the root is {} \nand the all the x during the iteration are: {}'.format(ans[0], ans[1]))
print('rate of convergence is linear')
plt.plot(range(len(ans[1])), ans[1])
plt.show()

print('\n\n\n\n')
def func2(x):
    return (x-1)**4

def func2deri(x):
    return 4*((x-1)**3)

ans = newton(func2, func2deri , 10)
print('the root is {} \nand the all the x during the iteration are: {}'.format(ans[0], ans[1]))
print('rate of convergence is linear')

plt.plot(range(len(ans[1])), ans[1])
plt.show()