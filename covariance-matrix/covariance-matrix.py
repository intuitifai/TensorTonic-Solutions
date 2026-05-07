import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    # We will work with a shortcut here.
    # 1. We will calculate mean for each column
    # 2. We will subtract mean from each value in that respective column
    # 3. We will get centered matrix X_c
    # 4. Just do mat mul for X_c and X_c transposed / number of elements in a column - 1
    # 5. Thats where we got our Covariance matrix
    X = np.asarray(X)
    N = X.shape[0]
    if N <= 1 or X.ndim <= 1:
        return None
    mean_col_wise = np.mean(X, axis=0)
    centered_matrix = X - mean_col_wise
    print()
    return np.matmul(centered_matrix.T, centered_matrix) / (N - 1)