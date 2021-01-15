import math, matplotlib.pyplot as plt
def computerError(n):
    f = math.factorial(n)
    a = math.sqrt(math.pi * 2 * n)*((n/math.e)**n)
    abe = abs(a - f)
    rle = abe/f * 1.0

    return abe, rle

abes = []
rles = []
for i in range(1, 16):

    temp = computerError(i)
    abes.append(temp[0])
    rles.append(temp[1])
    print(temp[0], temp[1])



plt.plot(list(range(1, 16)), abes, 'b.')
plt.xlabel('number as input')
plt.ylabel('abs error')
plt.show()

plt.plot(list(range(1, 16)), rles, 'r.')
plt.xlabel('number as input')
plt.ylabel('relative error')
plt.show()