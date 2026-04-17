def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp = 0
    total = len(y_true)
    for i, j in zip(y_true, y_pred):
        if i == j:
            tp += 1
            print(tp)
    return tp/total