def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    sum_val = 0
    sum_bin_count_p = sum(reference_counts)
    sum_bin_count_q = sum(production_counts)
    for p, q in zip(reference_counts, production_counts):
        norm_p = p / sum_bin_count_p
        norm_q = q / sum_bin_count_q
        sum_val += abs(norm_p - norm_q)
    score = sum_val / 2
    if score > threshold:
        return {"score": score, "drift_detected": True}
    return {"score": score, "drift_detected": False}
        