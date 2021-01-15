def euler(t0, x0, y0, dx_dt, dy_dt, h=0.0001, x_max=0.1):
    t = [t0]
    x = [x0]
    y = [y0]
    i = t0
    while i < x_max:

        yNext = y[-1] + h * dy_dt([x[-1], y[-1]])
        xNext = x[-1] + h * dx_dt([x[-1], y[-1]])
        # if xNext < 1 or yNext < 1:
        #     break
        i += h
        x.append(xNext)
        y.append(yNext)
        t.append(i)

    return x, y, t


