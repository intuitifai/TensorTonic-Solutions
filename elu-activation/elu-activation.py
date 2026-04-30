import math
import numpy as np

def elu(x, alpha):
    x = np.asarray(x)
    np_array =  np.where(x > 0, x, alpha * (np.exp(x) - 1))
    return np_array.tolist()