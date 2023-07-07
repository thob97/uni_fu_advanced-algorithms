import numpy as np
inf = float('inf')

#seidel algorithm
def apd(A, n: int):
    """Compute the shortest-paths lengths."""
    if all(A[i,j] for i in range(n) for j in range(n) if i != j):
        return A
    Z = A ** 2 + A

    B = np.matrix([
        [1 if i != j and (Z[i,j] > 0) else 0 for j in range(n)]
        for i in range(n)])
    
    T = apd(B, n)
    X = T*A
    degree = [sum(A[i,j] for j in range(n)) for i in range(n)]
    
    D = np.matrix([
        [2 * T[i,j] if X[i,j] >= T[i,j] * degree[j] else 2 * T[i,j] - 1 for j in range(n)]
        for i in range(n)])

    return D


def my_print(matrix):
    print("init:")
    print(matrix)
    print()
    print("result:")
    result = apd(matrix,len(matrix))
    print(result)

A = np.matrix([[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]])
B = np.matrix([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]])
C = np.matrix([
    [0,30,12],
    [0,0,17],
    [11,-6,0]
])


A5 = np.matrix([
    [0,30,12,5,2],
    [inf,0,17,-4,3],
    [11,-6,0,11,inf],
    [-2,7,inf,0,6],
    [3,1,6,inf,0]
])
my_print(A5)