#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        for key in a_dictionay.keys():
            if a_dictionary[key] == value:
                del a_dictionary[key]
    return a_dictionary
