import re


def count_unique_values(key_values):
    """
    Parameters
    ----------
    key_values = the values of the key you are looking for

    Returns a count of the unique occurrences of each value as a dictionary
    -------
    """

    pattern = re.compile(r"(left|right|spine|ambiguous|unidentifiable)",
                         re.IGNORECASE)  # define your pattern

    # iterate through of the values in key_values and apply a search for the
    # specified pattern
    matching_values = filter(pattern.search, key_values)

    # define the counts (starting off at 0
    counts = {"left": 0, "right": 0, "spine": 0, 'ambiguous': 0,
              'unidentifiable': 0}

    # for all the matching values, if they match, add to the appropriate
    # counts key/value pair
    for value in matching_values:
        if "left" in value.lower():
            counts["left"] += 1
        if "right" in value.lower():
            counts["right"] += 1
        if "spine" in value.lower():
            counts["spine"] += 1
        if "ambiguous" in value.lower():
            counts['ambiguous'] += 1
        if "unidentifiable" in value.lower():
            counts['unidentifiable'] += 1

    return counts
