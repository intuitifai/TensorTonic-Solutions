import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    if np.all(y_true == y_true[0]):
        if np.allclose(y_true, y_pred):
            return 1.0
        else:
            return 0.0
    mean_value = np.mean(y_true)
    error_mean_squared = np.sum((y_true - mean_value)**2)
    error_model_squared = np.sum((y_true - y_pred)**2)
    print(error_mean_squared)
    print(error_model_squared)
    # return None
    return (1 - (error_model_squared / error_mean_squared))