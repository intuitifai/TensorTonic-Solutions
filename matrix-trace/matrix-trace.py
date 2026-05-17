import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    # First, we get 2D -> 1D representation of A, then just sum it up! Simple ;)
    return np.sum(np.diag(A))
