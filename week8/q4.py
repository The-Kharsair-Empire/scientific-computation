from q1 import *
def evaluate(a, b, func):
    assert a < b, 'make sure a < b'
    interval = b-a
    ymax = 0
    for i in range(a, b):
        y = func(i)
        if y < 0:
            raise ValueError('not positive function')
        ymax = max(ymax, y)

    # ymax = ymax*1.1
    sample_size = 10000
    under = 0
    for j in range(sample_size):
        randx = sample(a, b)
        randy = sample(0, ymax)
        if func(randx) > randy:
            under += 1
    return under/sample_size

print(evaluate(-1, 1, lambda x: -x**2+1))