import sys
n = 1.0
p = n
while (n+1) > 1:
    p = n
    n /= 2


e = sys.float_info.epsilon
print('smallest number by my calculation: ',p)
print('smallest number ny system: ', e)