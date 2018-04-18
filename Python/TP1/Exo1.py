# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

def inverse(liste):
    res=""
    i=len(liste)
    while(i>0):
        res=res+liste[i-1]
        i=i-1
    return res
    #return liste[::-1]

def palindrome(phrase):
    phraseI=inverse(phrase)
    if(phrase==phraseI):
        return True
    else:
        return False


def position(mot,phrase):
    if(not(mot in phrase)):
        return None
    else:
        test=phrase.split(mot)
        return len(test[0])


chaine="je suis Jean Nemard"
print(inverse(chaine))
print(palindrome(chaine))
print(position("mard",chaine))
