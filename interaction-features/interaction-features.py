def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    final = []
    for arr in X:
        # final.append(arr)
        interim = arr.copy()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if i != j:
                    interim.append(arr[i] * arr[j])
        final.append(interim)
    print("here ")
    print(final)
    return final
            