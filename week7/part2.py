from matplotlib.pyplot import *
import numpy as np
beta = 0.0005
gamma = 0.1
delta = 0.01
eta = 0.02

def euler(f, s0, i0, r0, h=0.1, t0=0, tMax = 1000):
    stepSize = 1
    t = [t0]
    s = [s0]
    i = [i0]
    r = [r0]
    while t[-1] + stepSize < tMax:
        sNext = s[-1] + h*f[0](s[-1], i[-1], r[-1])
        iNext = i[-1] + h*f[1](s[-1], i[-1], r[-1])
        rNext = r[-1] + h*f[2](s[-1], i[-1], r[-1])
        t.append(t[-1] + stepSize)
        s.append(sNext)
        i.append(iNext)
        r.append(rNext)
    return s, i, r, t

def ds_dt(s, i, r):
    return -beta*s*i-delta*s+eta*s

def di_dt(s, i, r):
    return beta*s*i - gamma*i - delta*i+eta*i

def dr_dt(s, i, r):
    return gamma*i - delta*r+eta*r


s, i, r, t = euler([ds_dt, di_dt, dr_dt], 1000, 15, 0)
plot(t, s, label='s')
plot(t, i, label='i')
plot(t, r, label='r')
legend()
grid()
show()


c = 0
def phase_plane():
    def I(S, c):
        return gamma/beta*np.log(S)-S + c


    for c in [4, 7, 10, 20]:
        s = [0]
        i = [I(s[-1], c)]
        for j in range(1000):
            sNext = s[-1] + 1
            iNext = I(sNext, c)
            s.append(sNext)
            i.append(iNext)
        astring = 'c = {}'.format(c)
        plot(s, i, label=astring)

    legend()
    grid()
    show()

phase_plane()


