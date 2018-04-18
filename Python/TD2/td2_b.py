# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

def fibo() :
    f_n = 0
    f_n1 = 1
    while True :
        f_n,f_n1 = f_n1, f_n1 + f_n
        #if self.f_n <30 :
        yield f_n
        #else :
            #return


for f in fibo() :
    if f > 30 : break
    print f