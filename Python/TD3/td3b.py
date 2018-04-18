# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from time import *
from td3 import *

def memoize(f) :
    f.memotable = {}
    def new_f(*args):
        try:
            return f.memotable[args]
        except KeyError :
            result = f(*args)
            f.memotable[args]=result
            return result
    new_f.__doc__ = f.__doc__
    new_f.__name__ = f.__name__
    new_f.__dict__.update(f.__dict__)
    return new_f

@memoize
def test(x,y):
    sleep(2)
    return x+y

@memoize
def C(k,n):
    if k==0 or k==n :
        return 1
    else :
        return C(k-1,n-1) + C(k,n-1)



