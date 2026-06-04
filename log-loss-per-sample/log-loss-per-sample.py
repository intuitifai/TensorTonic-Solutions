import math
import numpy as np

def clip(y_pred, eps=1e-15):
    if y_pred < eps:
        return eps
    elif y_pred >= eps and y_pred <= 1 - eps:
        return y_pred
    else:
        return 1 - eps

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    result_loss = []
    for y_t, y_p in zip(y_true, y_pred):
        y_p = clip(y_p, eps)
        result_loss.append(-1 * (y_t * math.log(y_p) + (1 - y_t) * math.log(1 - y_p)))
    return result_loss