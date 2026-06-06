def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    final = []
    for k in values:
        interim = []
        for i in range(degree+1):
            interim.append(k**i)
        final.append(interim)
    return final