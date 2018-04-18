# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-
from random import choice
def quizz(capitales) :
    while len(capitales) > 0 :
        pays = choice( capitales.keys() )
        ville = yield pays
        if capitales[pays] == ville :
            print "Yes "
            del capitales[pays]
        else :
            print "No "

capitales  = {'Suisse':'Berne', 'Japon':'Tokyo'}
unQuizz = quizz(capitales)
try:
    unPays = unQuizz.next()
    while True :
        reponseVille = raw_input("Capitale de "+ unPays + " ? ")
        unPays = unQuizz.send(reponseVille)
except StopIteration :
    pass