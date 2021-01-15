from scipy.integrate import odeint
from matplotlib.pyplot import *
from euler import *
import numpy as np

a = 20
b = 5

def phase_plane(x0, y0, h=1, x_max=100):
    x = [x0]
    y = [y0]
    i = y0
    while i < x_max:
        yNext = y[-1] + h * b/a*x[-1]
        # if xNext < 1 or yNext < 1:
        #     break
        i += h
        y.append(yNext)
        x.append(i)

    return x, y

x, y = phase_plane(10, 15)
plot(x, y, label='phase plane')
legend()
grid()
show()



def dx_dt(P):
    return -a*P[1]

def dy_dt(P):
    return -b*P[0]*P[1]

x, y, t = euler(0, 10, 15, dx_dt, dy_dt)

plot(t, x, label='home')
plot(t, y, label='enemy')
legend()
grid()
show()




