#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    r_value = list(a_dictionary.keys())[0]
    b_score = list(a_dictionary.values())[0]
    for k, v in a_dictionary.items():
        if v > b_score:
            b_score = v
            r_value = k
    return (r_value)
