import numpy as np
A = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])

print('determinant caculated by python: ', np.linalg.det(A))


# result calculated by hand is 0, i think the reason of the error is similar to the precision of floating point?
