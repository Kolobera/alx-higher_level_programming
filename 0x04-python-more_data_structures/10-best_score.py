#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    maxi = max(a_dictionary.values())
    for i in a_dictionary.keys():
        if a_dictionary[i] == maxi:
            return i
