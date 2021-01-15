import numpy as np
A = np.array([[0, 6, -5], [0, 2, 7], [-4, 3, -7]])
b = np.array([-50, -30, 50])

x = np.linalg.solve(A, b)
print('coefficient matrix A is: \n', A, '\n')

for i in range(len(x)):
    out = 'X{} = {}'.format(i+1, x[i])
    print(out)

transpose = np.transpose(A)
print('the transpose is: \n', transpose, '\n')

inverse = np.linalg.inv(A)
print('the inverse is: \n', inverse, '\n')

