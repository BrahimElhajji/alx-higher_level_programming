#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary:
        max_v = max(a_dictionary.values())

        for k, v in a_dictionary.items():
            if v == max_v:
                return k
    else:
        return None
