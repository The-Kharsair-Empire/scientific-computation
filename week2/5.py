import math, matplotlib.pyplot as plt
def condition(x):
    conNum = x*(1+(math.tan(x))**2)/math.tan(x)
    return conNum

conList = []
x = list(range(1, 10000))
for i in x:
    conList.append(condition(i))

plt.plot(x, conList)
plt.xlabel('number as x')
plt.ylabel('condition number')
plt.show()
