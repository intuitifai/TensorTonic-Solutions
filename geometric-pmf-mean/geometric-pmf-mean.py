import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    k = np.asarray(k)

    # PMF
    pmf = ((1 - p) ** (k - 1)) * p

    # Mean
    mean = 1 / p

    return pmf, mean