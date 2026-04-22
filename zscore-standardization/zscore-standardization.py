import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    mean = np.mean(X, axis=axis, keepdims=True) # calculate mean
    std = np.std(X, axis=axis, ddof=0, keepdims=True) # ddof = 1 => N-1 denominator in std, since we are looking at population instead of sample, keep ddof = 0
    
    return (X - mean) /( std + eps)