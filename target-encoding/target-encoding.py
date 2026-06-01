def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    final = []
    dictionary = {}
    for category, target in zip(categories, targets):
        if category in dictionary:
            dictionary[category]["target"] += target
            dictionary[category]["category_count"] += 1
        else:
            dictionary[category] = {
                "target": target,
                "category_count": 1
            }

    print(dictionary)
    semi_final_dict = {}
    for category, dictionary in dictionary.items():
        semi_final_dict[category] = dictionary["target"] / dictionary["category_count"]
    print(semi_final_dict)

    final = []

    for category in categories:
        final.append(semi_final_dict[category])

    return final