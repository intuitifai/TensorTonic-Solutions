import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    # Since this is a single step operation only, I won't be using any loops
    # 1. Accumulate squared gradients
    g = np.asarray(g)
    G += g**2
    # 2. Update the parameter
    w = w - (lr / np.sqrt(G + eps)) * g
    # Return weight
    return w, G
    
    