import numpy as np


def gauss_elimination_with_pivoting(a, b):
    
    nrows = a.shape[0]
    if np.linalg.det(a) == 0:
        raise ValueError("Determinant is equal to 0. Guassian elimination does not produce unique solution.")
    if a.shape[0] != a.shape[1]:
        raise ValueError("Matrix must be a square matrix")
    
    solutions = np.zeros(nrows)

    # Augment the matrix
    matrix = np.concatenate((a, b), axis=1)

    # Sort in reverse order "Pivoting"    
    matrix = matrix[np.argsort(a[:,0])][::-1]

    # Get values below pivots equal to 0 by doing row ops
    for i in range(nrows - 1):
        matrix[i + 1] = matrix[i + 1] - (matrix[i + 1][i]/matrix[i][i])*matrix[i] 
    

    for i in range(nrows - 1, -1, -1):
        solutions[i] = (matrix[i][nrows] - np.dot(matrix[i][:3], solutions))/matrix[i][i] 
    
    return solutions

A = np.array([[0, -3, 7],
              [1, 2, -1],
              [5, -2, 0]], dtype=float)
B = np.array([[4],
              [0],
              [3]], dtype=float)


gauss_elimination_with_pivoting(A, B)