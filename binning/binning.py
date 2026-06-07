import math

def binning(values, num_bins):
    if not values:
        return []

    min_val = min(values)
    max_val = max(values)

    if min_val == max_val:
        return [0] * len(values)

    w = (max_val - min_val) / num_bins

    return [
        min(math.floor((value - min_val) / w), num_bins - 1)
        for value in values
    ]