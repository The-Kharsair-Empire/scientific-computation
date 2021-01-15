from scipy.integrate import odeint
from matplotlib.pyplot import *
import numpy as np
#
#
# hl = 3
#
# D = 1
#
# interval = 1

for D in [1, 10, 20]:
    for interval in [0.25, 0.75, 1, 10, 20]:
        for hl in [3, 10, 40, 48]:

            ka = 1

            ke = 0.693/hl

            Init = np.array([10, 0, 0])

            t = [i/4 for i in range(192*4+1)]

            def pulse(D, interval=0.25):
                if interval % 4 == 0:
                    return D
                else:
                    return 0




            simTime = 192
            t0 = 0
            I0 = 0
            P0 = 0
            U0 = 0
            I = [I0]
            P = [P0]
            U = [U0]
            i = t0
            t = [t0]

            while i < simTime:
                I.append(I[-1] + interval * (-ka * I[-1]) + pulse(D, t[-1]))
                P.append(P[-1] + interval * (ka * I[-1] - ke * P[-1]))
                U.append(U[-1] + interval * (ke * P[-1]))

                i += interval
                t.append(i)


            plot(t, I, label='intestine')
            plot(t, P, label='plasma')
            plot(t, U, label='urine')
            # axis([0, 25, 0, 25])
            s = 'd={}, in={}, hl={}'.format(D, interval, hl)
            title(s)
            #plot(t, Cp, label='plasma concentration')
            legend()
            # title("using euler's method")
            grid()
            show()




