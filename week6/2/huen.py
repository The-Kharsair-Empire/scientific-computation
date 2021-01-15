def huen(t0, I0, P0, U0, f1, f2, f3, interval = 0.25, simTime = 192):
    t = [t0, t0]
    I = [I0, I0]
    P = [P0, P0]
    U = [U0, U0]
    Cp = [P[-1]/70]*2
    i = t0
    while i < simTime:
        INext = I[-2] + interval/2*(f1([I[-1], P[-1], U[-1]])+f1([I[-2], P[-2], U[-2]]))
        PNext = P[-2] + interval/2*(f2([I[-1], P[-1], U[-1]])+f2([I[-2], P[-2], U[-2]]))
        UNext = U[-2] + interval/2*(f3([I[-1], P[-1], U[-1]])+f3([I[-2], P[-2], U[-2]]))

        i += interval
        I.append(INext)
        P.append(PNext)
        U.append(UNext)
        CpNext = P[-1] / 70
        Cp.append(CpNext)
        t.append(i)

    return t, I, P, U, Cp


def huen2(t0, I0, P0, U0, f1, f2, f3, p,  interval = 0.25, simTime = 192):
    t = [t0, t0]
    I = [I0, I0]
    P = [P0, P0]
    U = [U0, U0]
    Cp = [P[-1]/70]*2
    i = t0
    while i < simTime:
        INext = I[-2] + interval/2*(f1([I[-1], P[-1], U[-1]])+f1([I[-2], P[-2], U[-2]]))+p(I0, t[-1])
        PNext = P[-2] + interval/2*(f2([I[-1], P[-1], U[-1]])+f2([I[-2], P[-2], U[-2]]))
        UNext = U[-2] + interval/2*(f3([I[-1], P[-1], U[-1]])+f3([I[-2], P[-2], U[-2]]))

        i += interval
        I.append(INext)
        P.append(PNext)
        U.append(UNext)
        CpNext = P[-1] / 70
        Cp.append(CpNext)
        t.append(i)

    return t, I, P, U, Cp


