#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os, sys, types
from copy import *
import matplotlib.pyplot as plt


class Polynome(object):     # new class type (hérite de object) => fonctionnalités avancées

    def __init__(self, monomes):         # constructeur : initialise le dictionnaire
        self.monomes = monomes           # des monônes (dico vide => polynône nul)

    def __copy__(self):                             # renvoie un duplicata réel de l'object
        return Polynome(copy(self.monomes))         # -> appelé par l'opérateur copy( )


    def estNul(self):       # renvoyer True si polynône nul
        return len(self.monomes) == 0  # à faire

    def degre(self):        # renvoyer le degré du polynône (None si polynône nul)
        if(self.estNul()):
            return None
        else :
            return max(self.monomes.keys())


    @property                           # décoration (surcharge) de l'accès :
    def monomes(self):                  # self.monomes renvoie une copie du dictionnaire
        return copy(self.__monomes)     # privé self.__monomes

    @monomes.setter                                 # décoration (surcharge) de l'affectation :
    def monomes(self, monomes) :                    # self.monomes = ...
        if type(monomes) <> types.DictionaryType :
            raise TypeError
        else :                          # -> vérifie le type des clés k et des valeurs ak
                for cle in monomes.keys() :      # -> et supprime les valeurs ak nulles
                    if type(cle) <> types.IntType or type(monomes[cle]) <> types.IntType:
                        raise TypeError
                    elif (monomes[cle] == 0):
                        del monomes[cle]
        self.__monomes = monomes    # recopie les monomes significatifs dans l'attribut privé


    def __getitem__(self, k):           # surcharge de accès à :  self[k]
        return self.__monomes.get(k,0)  # -> retourne le coeff ak du monône de deg k

    def __delitem__(self, k):           # surcharge de la suppression :  del self[k]
        if self.__getitem__(k) == 0 :
            raise Error
        else :
            del self.__monomes[k]                 # -> supprime le monône de deg k

    def __setitem__(self, k, ak):       # surcharge de l'affectation de :  self[k]
        if type(ak)<>types.IntType:
            raise TypeError
        if ak == 0:
            self.__delitem__(k)                 # !! si ak = 0  ->  supression du monône ...
        else :
            self.__monomes[k]=ak



    def __iter__(self):                             # itérateur permettant
        self.degres = sorted(self.monomes.keys())   # de parcourir les couples
        return self                                 # (val, deg) des monônes
                                                    # du polynône par ordre
    def next(self):  # décroissant de degré
        if(len(self.degres)==0):
            raise StopIteration
        else:
            axi = self.degres.pop()
            return self.__monomes[axi],axi




    @staticmethod               # méthode statique qui retourne la chaine
    def str_monome(ak,k):       # 'ak*X**k'  à partir du coefficient ak et
        if k==0 :               # du degré k d'un monôme en prenant en compte
            return str(ak)      # tous les cas particuliers :
        else :                  # k=0, k=1, signe de ak, ...
            res = ""
            if(ak==1):
                if(k==1):
                    return res +"X"
                else :
                    return res +"X**"+str(k)
            else:
                if(k==1):
                    return res +str(ak)+"*X"
                else:
                    return res +str(ak)+"*X**"+str(k)


    def __repr__(self):             # retourne la chaine 'representant' le polynône
        return self.__str__()       # __repr__ est uitilisé lors de l'évaluation
                                    # directe à l'interpréreur, __str__ lors
    def __str__(self):              # d'un print ou d'une conversion par str( )
        res = ""
        degre = max(self.__monomes)
        for ak,k in self :
            if(k == degre):
                res = res + self.str_monome(ak,k)
            else:
                if(ak>0):
                    res = res + "+" + self.str_monome(ak,k)
                else :
                    res = res + self.str_monome(ak,k)
        return res


    def __pos__(self):          # surcharge de l'opérateur unaire :  + self
        return copy(self)       # -> renvoie un duplicata

    def __neg__(self):          # surcharge de l'opérateur unaire :  - self
        monome = copy(self)
        for degree in monome.keys():
            monome[degree] = - monome[degree]
        return monome

    def __add__(self, Q):       # surcharge de l'opérateur binaire :  self + Q
        monome = copy(self)
        if type(Q)==types.IntType or type(Q)==types.FloatType:
            monome[0]= monome[0]+Q
            return monome
        elif isinstance(Q,Polynome):
            monomeQ = copy(Q)
            for val,deg in monomeQ:
                print str(deg)
                if deg in monome.keys():
                    monome[deg] = monome[deg] + val
                else:
                    monome[deg] = val
            return monome
        else :
            raise TypeError # en prenant en compte les cas Q polynôme ou nombre

    def __radd__(self, x):      # surcharge de l'opérateur binaire :  x + self
        return self + x # avec x un nombre (entier ou flottant)

    def __sub__(self, Q):       # surcharge de l'opérateur binaire :  self - Q
        monome = copy(self)
        if type(Q)==types.IntType or type(Q)==types.FloatType:
            monome[0] += -Q
            return monome
        elif isinstance(Q,Polynome):
            for val,deg in Q:
                    monome[deg] += - val
            return monome
        else :
            raise TypeError         # en prenant en compte les cas Q polynôme ou nombre

    def __rsub__(self, x):      # surcharge de l'opérateur binaire :  x - self
        return - self + x         # avec x un nombre (entier ou flottant)

    def __mul__(self, Q):       # surcharge de l'opérateur binaire :  self * Q
        monome = copy(self)
        monomeR = Polynome({})
        if type(Q)==types.IntType or type(Q)==types.FloatType:         # en prenant en compte les cas Q polynôme ou nombre P = -x+1 et Q = x+2 et -3*P * Q *(x-3)
            for val, deg in monome:
                monome[deg] = val*Q
            return monome
        elif isinstance(Q,Polynome):
            for val,deg in monome :
                for val2, deg2 in Q:
                    monomeR[deg+deg2] += val*val2
            return monomeR
        else:
            raise TypeError


    def __rmul__(self, x):      # surcharge de l'opérateur binaire :  x * self
        return self*x       # avec x un nombre (entier ou flottant)

    def __pow__(self, n):                           # surcharge de l'opérateur binaire :  self ** n
        monome = copy(self)
        if n<0:
            raise ArithmeticError
        elif n == 0:
            return 1
        elif type(n)==types.IntType or type(n)==types.FloatType:
            for i in range(1,n):
                monome *= self
            return monome
        else:
            raise TypeError


    def __eq__(self,Q):         # surcharge de l'opérateur binaire :  self == Q
        monome = copy(self)
        if type(Q)==types.IntType or type(Q)==types.FloatType:        # en prenant en compte les cas Q polynôme ou nombre
            if max(monome)>0:
                return False
            elif monome[0]== Q:
                return True
            else:
                return False
        elif isinstance(Q,Polynome):
            equ = True
            for val,deg in monome :
                if Q[deg] <> val :
                    equ = False
            for val,deg in Q :
                if monome[deg] <> val :
                    equ = False
            return equ
        else:
            raise TypeError

    def __ne__(self,Q):         # surcharge de l'opérateur binaire :  self <> Q
        return not(self ==Q)  # à faire         # en prenant en compte les cas Q polynôme ou nombre


    def __call__(self,x):       # surcharge de l'appel fonctionnel :  self(x)
        h = 0        # x étant de nature quelconque ...
        for ak,k in self:
            h = h+(x*ak)**k
        return h

    def __int__(self):          # surcharge de la conversion :  int(self)
        for val, deg in self:
            if deg <> 0:
                raise TypeError
            else:
                return self[val]        # (uniquement si polynôme constant)

    def __float__(self):        # surcharge de la conversion :  float(self)
        pass  # à faire         # (uniquement si polynôme constant)


    def derivee(self):
    	monome = copy(self)
    	res = Polynome({})
    	for val, deg in monome:
			if (deg != 0):
				res[deg-1] = val * deg
        return res

	def primivite(self):
		monome = copy(self)
		res = Polynome({})
		for val,deg in monome:
			if deg == 0:
				res[1] = val
			else:
				res[deg+1] = val * 1/deg
		return res

	def calculVal(self,x):
		res = 0
		for val, deg in self:
			res += val*x**deg
		return res

    def graphe(self,a,b):
        tabx = []
        taby = []
        for x in range(a,b):
            tabx.append(x)
            taby.append(self(x))
            print x
            print self(x)
        plt.title("Graphe :")
        plt.plot(tabx,taby)
        plt.show()










X = Polynome({1:1})   # Définition d'un object monôme X
