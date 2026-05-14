import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x)
    mean = np.mean(x)
    variance = np.sum((x - mean)**2) / (len(x) - 1)
    std_dev = np.sqrt(variance)
    return variance, std_dev
    