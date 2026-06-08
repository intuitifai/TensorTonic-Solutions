def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    final = []
    for value in values:
        final.append(ordering.index(value))
    return final