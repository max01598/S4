# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

class fibo() :
    def __init__(self) :
        self.f_n = 0
        self.f_n1 = 1
    def __iter__(self) :
        return self
    def next(self) :
        self.f_n,self.f_n1 = self.f_n1, self.f_n1 + self.f_n
        #if self.f_n <30 :
        return self.f_n
        #else :
            #raise StopIteration


for f in fibo() :
    if f > 30 : break
    print f
