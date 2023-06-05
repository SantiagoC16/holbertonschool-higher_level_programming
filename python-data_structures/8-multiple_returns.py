#!/usr/bin/python3
def multiple_returns(sentence):
    var = len(sentence)
    last = sentence[0]
    if sentence:
        return_tuple = (var, last)
        return return_tuple
    else:
        return_tuple = (var, None)
        return return_tuple
