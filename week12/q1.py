import numpy as np

def dominance(matrix_a, matrix_b):
    (row, column) = np.shape(matrix_a)
    table = [[0 for _ in range(column)] for _ in range(row)]
    for i in range(row):
        for j in range(column):
            table[i][j] = [matrix_a[i, j], matrix_b[i, j]]
    print(table)
    loop = True
    row_column = 1
    while loop:
        loop = False
        if row_column == 1:
            new_list = []
            for i in range(column):
                tmp = []
                for j in range(row):
                    tmp.append(table[j][i][0])
                new_list.append(tmp.index(max(tmp)))
            a_list = []
            for i in range(row):
                a_list.append(i)
            for i in new_list:
                if i in a_list:
                    a_list.remove(i)
            for i in range(len(a_list), 0, -1):
                del(table[a_list[i-1]])
                row -= 1
                loop = True
            print(table)
            if len(table[0]) == 1:
                print('Nash')
        else:
            new_list = []
            for i in range(row):
                tmp = []
                for j in range(column):
                    tmp.append(table[i][j][1])
                new_list.append(tmp.index(max(tmp)))
            a_list = []
            for i in range(column):
                a_list.append(i)
            for i in new_list:
                if i in a_list:
                    a_list.remove(i)
            for i in range(len(a_list), 0, -1):
                for j in range(row):
                    del (table[j][a_list[i - 1]])
                column -= 1
                loop = True
            print(table)

            if len(table[0]) == 1:
                print('Nash')
        row_column *= -1
    print('==========================')

a = np.matrix([[0, 3, 2], [1, 2, 4], [2, 4, 3]])
b = np.matrix([[2, 1, 3], [4, 1, 1], [1, 4, 2]])
c = np.matrix([[5, 7, 2], [8, 6, 5], [1, 8, 4]])
d = np.matrix([[5, 8, 1], [7, 6, 8], [2, 5, 4]])
dominance(a, b)
dominance(d, b)
dominance(a, c)
dominance(b, d)
dominance(c, d)