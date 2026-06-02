def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    # Write code here
    final = []
    for request_dict in requests:
        if request_dict["user_id"] in feature_store:
            avg_spend_total_orders = feature_store[request_dict["user_id"]]
            online_features = request_dict["online_features"]  
        else:
            avg_spend_total_orders = defaults
            online_features = request_dict["online_features"]
        final.append(avg_spend_total_orders | online_features)
    return final
    