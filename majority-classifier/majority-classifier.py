import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    X_test = np.asarray(X_test)
    y_train = np.asarray(y_train)
    values, counts = np.unique(y_train, return_counts=True)
    most_freq = values[counts.argmax()]
    print(most_freq)
    X_test.fill(most_freq)
    return X_test