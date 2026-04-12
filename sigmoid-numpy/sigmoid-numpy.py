import numpy as np

def sigmoid(x):
    x = np.asarray(x) # this would basically convert the list to an ndarray in numpy
    return 1 / (1 + np.exp(-x)) # bye-bye for loops, we don't care about how many nested loops are there, np will take care of them
    