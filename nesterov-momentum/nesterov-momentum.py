import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):

    w = np.asarray(w)
    v = np.asarray(v)
    grad = np.asarray(grad)

    # Look-ahead
    look_w = w - momentum * v

    # Velocity
    v = momentum * v + lr * grad

    # Weight update
    w = w - v

    return w, v