import copy
import numpy as np

inf = float('inf')

def FloydWarshall (matrix):
    n = len(matrix)

    #path matrix is simmilar to initial matrix
    path = copy.deepcopy(matrix)
    path = createPath_Matrix(path)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                old = matrix[i,j]
                matrix[i,j] = min (matrix[i,j], matrix[i,k]+matrix[k,j])
                
                #if a new min was found update the path
                if (old != matrix[i,j]):
                    
                        path[i,j] = path[i,k]

    return (matrix,path)


def createPath_Matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i,j] != inf:
                matrix[i,j] = j
            
    return matrix




#
#seidel
def aadp(A):
    #tests if A is 1 for all i!=j
    counter = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i!=j and (A[i,j] == 1):
                counter +=1
    if counter == ( len(A)*len(A)-len(A) ):
        return A

    #calculates B matrix (connections)
    Z = A*A+A
    B = Z
    for i in range(len(Z)):
        for j in range(len(Z)):             ########
            if i!=j and (Z[i,j] >= 1 or A[i,j]==1):
                B[i,j] = 1
            else:
                B[i,j] = 0

    T = aadp(B)
    D = T
    X = T*A

    degree = [sum(A[i,j] for j in range(len(T))) for i in range(len(T))]

    #calculates D (distances from recursions) with help of X
    for i in range(len(T)):
        for j in range(len(T)):           ### j
            if X[i,j] >= T[i,j] * degree[j]:
                D[i,j] = T[i,j] * 2
            else: 
                D[i,j] = T[i,j] * 2 -1
    return D




"""
A = np.matrix([[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]])
print(aadp(A))

#B = [[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]]
#print( aadp(B,Degree) )
"""

#Alp3 second u22 121

A2 = np.matrix([
    [0,30],
    [inf,0]
])

A3 = np.matrix([
    [0,30,12],
    [inf,0,17],
    [11,-6,0]
])

A4 = np.matrix([
    [0,30,12,5],
    [inf,0,17,-4],
    [11,-6,0,11],
    [-2,7,inf,0]
])

A5 = np.matrix([
    [0,30,12,5,2],
    [inf,0,17,-4,3],
    [11,-6,0,11,inf],
    [-2,7,inf,0,6],
    [3,1,6,inf,0]
])


result,path = FloydWarshall(A5)
print(result)
print(path)
