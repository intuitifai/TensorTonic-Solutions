import numpy as np
from scipy.special import comb

def get_pmf(n, p, k):
    return comb(n, k) * p**k * (1-p)**(n-k)

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf = get_pmf(n, p, k)
    cdf = 0.0
    for i in range(0, k+1):
        cdf += get_pmf(n, p, i)
    return float(pmf), float(cdf)