import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    
    # Initialize vector with zeros
    vector = np.zeros(len(vocab), dtype=int)
    
    # Count occurrences of each vocab word in tokens
    for i, word in enumerate(vocab):
        vector[i] = tokens.count(word)
    
    return vector