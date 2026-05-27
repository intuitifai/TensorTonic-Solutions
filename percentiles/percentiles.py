import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    
    Parameters:
        x : array-like
            Input data
        q : float or array-like
            Percentile(s) to compute (0–100)
    
    Returns:
        Percentile value(s)
    """
    x = np.sort(np.asarray(x))
    q = np.asarray(q)

    n = len(x)
    if n == 0:
        raise ValueError("Input array is empty")

    # Convert percentile to position
    pos = (q / 100) * (n - 1)

    lower = np.floor(pos).astype(int)
    upper = np.ceil(pos).astype(int)

    # Handle exact indices
    weight = pos - lower

    result = (1 - weight) * x[lower] + weight * x[upper]

    return result