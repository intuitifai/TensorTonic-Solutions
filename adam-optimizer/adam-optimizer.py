import numpy as np
import math

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param_new = []
    m_new = []
    v_new = []
    for i in range(len(param)):
        print(m[i])
        # update momentum
        new_m = (beta1 * m[i]) + (1 - beta1) * grad[i]
        # update velocity
        new_v = (beta2 * v[i]) + (1 - beta2) * (grad[i])**2
        # bias correction
        bias_corrected_m = new_m / (1 - beta1**t)
        bias_corrected_v = new_v / (1 - beta2**t)
        # parameter update
        new_param = param[i] - (lr * (bias_corrected_m) / (math.sqrt(bias_corrected_v) + eps))
        # just append everything
        param_new.append(new_param)
        m_new.append(new_m)
        v_new.append(new_v)
    return param_new, m_new, v_new