def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    value_dict = {}
    final = []
    
    for value in values:
        if value in value_dict:
            value_dict[value] += 1
        else:
            value_dict[value] = 1
            
    total_sum_values_count = 0
    for k, v in value_dict.items():
        total_sum_values_count += v
    
    for value in values:
        for k, v in value_dict.items():
            if k == value:
                final.append(v/total_sum_values_count)

    return final