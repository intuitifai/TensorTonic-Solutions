def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    stopwords_set = set(stopwords)
    filtered = [word for word in tokens if word not in stopwords_set]
    return filtered