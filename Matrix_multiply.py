#import numpy as np

def matrix_mult(a, b):
    m = len(a)  # a: m × n
    n = len(b)  # b: n × k
    k = len(b[0])
    c = [[None for __ in range(k)] for __ in range(m)]  # c: m × k
    for i in range(m):
        for j in range(k):
            c[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))
    return c

#   return (np.matrix(a) * np.matrix(b)).tolist()


m1= [ [1, 2, 3],
    [3, 2, 1],
    [2, 1, 3] ]
m2 =[ [4, 5, 6],
    [6, 5, 4],
    [4, 6, 5] ]

pprint(matrix_mult(m1,m2))

