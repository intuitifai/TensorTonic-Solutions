import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X)
    min_X = np.min(X, axis=axis, keepdims=True)
    max_X = np.max(X, axis=axis, keepdims=True)
    denom = max_X - min_X
    denom = np.where(denom==0, eps, denom)
    return (X - min_X) / denom
    