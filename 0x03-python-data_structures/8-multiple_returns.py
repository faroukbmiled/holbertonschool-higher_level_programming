#!/usr/bin/python3
def multiple_returns(sen):
    if sen != "":
        return ((len(sen), sen[0]))
    else:
        return ((0, None))
