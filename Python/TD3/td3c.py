# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import sys

def debug(f) :
    def new_f(*args,**kwargs) :
        print "***Appel de la fonction", f.__name__
        print "***              args :", args
        print "***              kwargs :", kwargs
        try :
            result = f(*args,**kwargs)
        except Exception, e :
            print "***Erreur ",f.__name__
            print "***       ",e
            raise e
        else :
            if result == None :
                print "*** pas de résultat "
            else :
                print "Resultat ",result
                return result
    new_f.__doc__ = f.__doc__
    new_f.__name__ = f.__name__
    new_f.__dict__.update(f.__dict__)
    return new_f