# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-


def trier(n,liste):
    if(len(liste)==0):
        return None
    if(n==len(liste)):
        return None
    else:
        min = liste[0]
        listeracc= liste[0:len(liste)-n]
        for num in listeracc:
            if(num<min):
                min=num
        liste.remove(min)
        liste.append(min)
        n=n+1
        trier(n,liste)
lis = [7,8,2,1]
print lis
trier(0,lis)
print lis

lis = ["bonjour","coucou","alphabet"]
print lis
trier(0,lis)
print lis