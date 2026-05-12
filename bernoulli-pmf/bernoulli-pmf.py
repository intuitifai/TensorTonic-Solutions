import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.asarray(x)
    x = np.where(x==1, p, 1-p)
    mean = p
    var = mean * (1-mean)
    return x, mean, var