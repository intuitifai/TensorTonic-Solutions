import math

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    # Computing cosine similarity
    numerator = sum(a*b for a, b in zip(x1, x2))
    x1_norm = math.sqrt(sum(x**2 for x in x1))
    x2_norm = math.sqrt(sum(x**2 for x in x2))
    if x1_norm != 0 and x2_norm != 0:
        cosine_similarity = numerator / (x1_norm * x2_norm)
        if label == 1:
            return 1 - cosine_similarity
        elif label == -1:
            return max(0, cosine_similarity - margin)
    