import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length safely and efficiently.
    Works for a single 1D vector or a 2D array of multiple vectors.
    """
    # Force input into a NumPy array
    v = np.asarray(v, dtype=float)
    
    # Calculate the length (norm) along the last axis (axis=-1)
    # keepdims=True ensures the dimensions align perfectly for division later
    denom = np.linalg.norm(v, axis=-1, keepdims=True)
    
    # Avoid division by zero: if length < 1e-8, set denominator to 1 (leaves 0 as 0)
    # Or swap it with your eps_8 value directly depending on your goal
    denom = np.where(denom < 1e-8, 1.0, denom)
    
    return v / denom
