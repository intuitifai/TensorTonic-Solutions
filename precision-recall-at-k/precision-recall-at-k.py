def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended_k = recommended[:k] #only top-k
    common = list(set(recommended_k).intersection(set(relevant)))
    return [len(common)/k, len(common)/len(relevant)] # [precision, recall]