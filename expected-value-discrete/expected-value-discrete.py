import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    # lets raise ValueError if probabilities sum is not 1
    if sum(p) != 1.0 or (1.0 - sum(p)) > 0.000001:
        raise ValueError("Probabilities sum not equals to 1")
    expectation = 0.0
    if x.shape == p.shape:
        for i in range(len(x)):
            expectation += x[i] * p[i]    
    return expectation
