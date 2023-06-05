#!/usr/bin/python3
def multiple_returns(sentence):
    var = len(sentence)
    if sentence:
        last = sentence[0]
        return_tuple = (var, last)
        return return_tuple
    else:
        return_tuple = (var, None)
        return return_tuple
