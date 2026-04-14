import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    s = np.asarray(s)
    w = np.asarray(w)
    g = np.asarray(g)
    new_w = []
    new_s = []
    for i in range(len(w)):
        # calculate running average
        s_new = (beta * s[i]) + ((1 - beta) * (g[i]**2))
        # parameter update
        w_new = w[i] - (lr / (np.sqrt(s_new + eps))) * g[i]
        new_s.append(s_new)
        new_w.append(w_new)
    return new_w, new_s