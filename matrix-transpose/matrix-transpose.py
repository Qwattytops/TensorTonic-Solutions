import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    #Get original dimensions
    A = np.array(A)
    N, M = A.shape
    transpose = np.zeros((M, N), dtype=A.dtype)

    for i in range(N):
        for j in range(M):
            transpose[j, i] = A[i,j]
    return transpose
    pass
