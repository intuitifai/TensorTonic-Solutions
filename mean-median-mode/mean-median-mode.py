import numpy as np

def mean_median_mode(x):
    x = np.asarray(x)
    vals, counts = np.unique(x, return_counts=True)
    mode = vals[np.argmax(counts)]
    
    return np.mean(x), np.median(x), mode