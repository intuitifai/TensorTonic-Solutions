import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if y is not None and len(y) != 0:
        values, counts = np.unique(y, return_counts=True)
        entropy = 0
        for i in range(len(values)):
            p = counts[i] / sum(counts)
            entropy += -1 * p * np.log2(p)
        return entropy
    return 0.0