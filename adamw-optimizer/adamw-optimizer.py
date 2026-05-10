import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    # Write code here
    # Making sure every list becomes an ndarray
    w = np.asarray(w)
    m = np.asarray(m)
    v = np.asarray(v)
    grad = np.asarray(grad)
    # 1. Let's update the first moment
    m = beta1 * m + (1 - beta1) * grad
    # 2. Update the velocity
    v = beta2 * v + (1 - beta2) * grad**2
    # 3. Update AdamW parameter
    w = w - lr * weight_decay * w - lr * m / np.sqrt(v + eps)
    return w, m, v
    