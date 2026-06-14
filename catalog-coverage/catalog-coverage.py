def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    unique = []
    for rec in recommendations:
        for item in rec:
            if item not in unique:
                unique.append(item)
    return len(unique) / n_items