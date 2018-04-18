# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

class GenericContainer :
    def __init__(self,**kwargs) :
        for cle in kwargs :
            settattr(self,cle,kwargs[cle])