import math
for i in [0, 1, 0.1]:
    current = 1
    a = 1

    while (a < 15):
        prev = current
        current += i** a/math.factorial(a)
        ea = (current - prev)/current * 1.0
        print('for x = {}, polynormial = {}'.format(i, a), ', the error is: ', ea)
        a += 1


