import numpy as np
A = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
b = np.array([0.1, 0.3, 0.5])

x = np.linalg.solve(A, b)
print('coefficient matrix A is: \n', A, '\n')

for i in range(len(x)):
    out = 'X{} = {}'.format(i+1, x[i])
    print(out)