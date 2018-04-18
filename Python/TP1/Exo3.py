# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

def inverse(dico):
    dico_inverse=dict()
    for key,value in dico.items():
        if(dico_inverse.has_key(value)):
            dico_inverse[value]+=" "+key
        else:
            dico_inverse[value]=key
    return dico_inverse

dico = {'paul':20 , 'pierre':25, 'jean':20, 'eric':20, 'marc':25 }
print(inverse(dico))

