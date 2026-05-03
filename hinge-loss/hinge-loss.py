import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    y_true_y_score_per_element = y_true * y_score
    margin_score = margin - y_true_y_score_per_element
    loss_per_element = np.maximum(0, margin_score)
    if reduction == "mean":
        return np.mean(loss_per_element)
    else:
        return np.sum(loss_per_element)