import numpy as np
from matplotlib.pyplot import *
def sample_time(lambda_):
    return -np.log(np.random.random())/lambda_


beta = 0.0002
delta = 0.0002
f = 0.0005
alpha = 0.1

S = 500
I = 25
R = 4475

def e1():
    global S
    S += beta * (I + R + S)

def e2():
    global S, I
    I += f * S * I
    S -= f * S * I

def e3():
    global S
    S -= delta * S

def e4():
    global R, I
    R += alpha * I
    I -= alpha * I

def e5():
    global I
    I -= delta * I

def e6():
    global R
    R -= delta * R

events = [e1, e2, e3, e4, e5, e6]
x = [0]
susceptible = [S]
infected = [I]
recovered = [R]
i = 0
while i < 500000:
    p = [beta * (I + R + S), f * S * I, delta * S, alpha * I, delta * I, delta * R]
    total = sum(p)
    p = list(map(lambda x: x/total, p))
    j = 0
    the_min = j
    # print(p)
    t = sample_time(p[0])
    while j < len(p):
        if sample_time(p[j]) < t:
            t = sample_time(p[j])
            the_min = j
        j += 1
    # print(t)


    events[the_min]()

    x.append(x[-1]+t)
    susceptible.append(S)
    infected.append(I)
    recovered.append(R)
    i += t


plot(x, susceptible, label="susceptible")
plot(x, infected, label='infected')
plot(x, recovered, label='recovered')
legend()
grid()
show()

# t1 = [0]
# for i in range(10000):
#     p = [np.random.random() for _ in range(6)]
#     tNext = min([sample(i) for i in p])
#     t1.append(t1[-1]+tNext)
#
# t2 = [0]
# for i in range(10000):
#     p = [np.random.random() for _ in range(6)]
#     tNext = min([sample(i) for i in p])
#     t2.append(t2[-1]+tNext)
#
# print(t1==t2)