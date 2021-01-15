from task2 import *
from math import sqrt, sin
import numpy as np
from matplotlib.pyplot import *
from task1 import euler

# huen: b=1/2
# midpoint: b=1
# Ralston: b=2/3

def ODE1(x, y):
    return x * np.sqrt(1-(y-4)**2)

def ODE2(x, y):
    return y**3

def solve1():
    for h in [0.1, 0.05, 0.025, 0.0125]:
        a = RK2(ODE1, 0.5, h, 4, 0, 1.5, 0.1)
        s = "h = {}, b = {}, RK2".format(h, 0.5)
        plot(a[0], a[1], label=s)
        a = euler(ODE1, 0.5, h, 4, 0, 1.5, 0.1)
        s = "h = {}, b = {}, euler".format(h, 0.5)
        plot(a[0], a[1], label=s)
solve1()


def exactFunc1(x):
    return sin(x**2/2)+4

def drawExactFunc1():
    stepSize = 0.1
    x = [0]
    y = [exactFunc1(0)]
    while x[-1]+stepSize < 1.5:
        xi = x[-1]+stepSize
        yi = exactFunc1(xi)
        y.append(yi)
        x.append(xi)

    plot(x, y, label='exact function for ODE1')
    legend()
    grid()
    show()

drawExactFunc1()



def solve2():
    for h in [0.1, 0.05, 0.025, 0.0125]:
        a = RK2(ODE2, 0.5, h, 1, 0, 0.45, 0.1)
        s = "h = {}, b = {}, RK2".format(h, 0.5)
        plot(a[0], a[1], label=s)
        a = euler(ODE2, 0.5, h, 1, 0, 0.45, 0.1)
        s = "h = {}, b = {}, euler".format(h, 0.5)
        plot(a[0], a[1], label=s)
solve2()

def exactFunc2(x):
    return 1/np.sqrt(1-2*x)

def drawExactFunc2():
    stepSize = 0.1
    x = [0]
    y = [exactFunc2(0)]
    while x[-1] + stepSize < 0.5:
        xi = x[-1] + stepSize
        yi = exactFunc2(xi)
        y.append(yi)
        x.append(xi)

    plot(x, y, label='exact function for ODE2')
    legend()
    grid()
    show()
drawExactFunc2()
