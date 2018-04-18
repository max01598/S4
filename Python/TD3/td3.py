# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-
from time import sleep, time
from contextlib import contextmanager


class chrono :
    def __enter__(self):
        self.debut = time()

    def __exit__(self, type, value, traceback) :
        if type <> None :
            print "Erreur ",value
        print "Temps écoulé : ", time() -self.debut
        return True


@contextmanager
def chrono2():
    debut = time()
    yield
    print "TPS ecoulé :", time() - debut



with chrono2():
    for i in range(3):
        print i
        sleep(5)