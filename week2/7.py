import sys
n = 1.0
p = n
while n > 0:
    p = n
    n /= 2

print('smallest number before computer cannot distiguish it: ',p)
print('', p == sys.float_info.min*sys.float_info.epsilon)

