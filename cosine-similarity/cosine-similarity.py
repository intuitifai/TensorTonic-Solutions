import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)

    # Let's check if we get all [0] vector
    if np.all(a == 0) or np.all(b == 0):
        return 0
    dot_product = np.dot(a, b)
    a_l2_norm = np.linalg.norm(a)
    b_l2_norm = np.linalg.norm(b)
    return dot_product / (a_l2_norm * b_l2_norm)