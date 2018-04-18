#!/usr/bin/env python
# -*- coding: utf8 -*-
import webapp2, os, random, blagnac


class Participant:
    def __init__(self, nom):
        self.nom = nom              # nom du participant
        self.numCible = 1           # numero de sa prochaine cible a atteindre
        self.latitude = None        # latitude actuelle du participant
        self.longitude = None       # longitude actuelle du participant
        self.messages = []          # file des messages recus en attente de lecture


class Cible:
    def __init__(self, **kwargs):
        self.nom = kwargs['nom']
        self.latitude = kwargs['lat']
        self.longitude = kwargs['lon']


class Course(webapp2.RequestHandler):
    # Initialisation des attributs de classe (statiques)
    enCours = False         # booleen
    participants = None     # dictionnaire de cles nom et valeurs Participant
    cibles = None           # liste de 3 cibles
    vainqueur = None        # vainqueur de la course lorsque connu

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        try :
            cmd = self.request.get('cmd')
            nom = self.request.get('name').encode()
            if cmd == 'isRaceOnProgress':
                self.response.write(Course.enCours)
            elif cmd == 'reinitRace':
                Course.enCours = True
                Course.participants = {}
                Course.vainqueur = None
                Course.cibles = []
                lieuxCibles = random.sample(blagnac.lieux, 3)
                for lieu in lieuxCibles:
                    Course.cibles.append(Cible(nom=lieu['nom'], lat=lieu['lat'], lon=lieu['lon']))
                self.response.write("Ok")
            elif cmd == 'stopRace':
                try:
                    Course.enCours = False
                    self.response.write("Ok")
                except:
                    self.response.write("Prb stop")
            elif cmd == 'addParticipant':
                try:
                    p = Participant(nom)
                    Course.participants[nom] = p
                    self.response.write("Ok")
                except:
                    self.response.write("Prb aj")
            elif cmd == 'removeParticipant':
                try:
                     del Course.participants[nom]
                     self.response.write("Ok")
                except:
                    self.response.write("Prb rv")
            elif cmd == 'getParticipants':
                try:
                    res = ""
                    res = ",".join(Course.participants)
                    self.response.write(res)
                    #for p in Course.participants.keys():
                    #    res = res + str(p) + ","
                    #self.response.write(res)
                except:
                    self.response.write("Prb aff")
            elif cmd == 'getPosition':
                try:
                    self.response.write(str(Course.participants[nom].latitude)+","+str(Course.participants[nom].longitude))
                except:
                    self.response.write("Prb gPos")
            elif cmd == 'setPosition':
                try:
                    Course.participants[nom].latitude = self.request.get('lat').encode()
                    Course.participants[nom].longitude = self.request.get('lon').encode()
                    self.response.write("Ok")
                except:
                    self.response.write("Prb sP")
            elif cmd == 'sendMessage':
                try:
                    Course.participants[nom].messages.append(self.request.get('msg').encode())
                    self.response.write("Ok")
                except:
                    self.response.write("Prb sendM")
            elif cmd == 'getMessage':
                try:
                    #mes = Course.participants[nom].messages[-1]
                    #del Course.participants[nom].messages[-1]
                    mes = Course.participants[nom].messages[0]
                    del Course.participants[nom].messages[0]
                    self.response.write(mes)
                except:
                    self.response.write("Prb getM")
            elif cmd == 'getGoal' :
                try:
                    p = Course.participants[nom]
                    cible = Course.cibles[p.numCible-1]
                    self.response.write(str(cible.nom) + "," + str(cible.latitude) + "," + str(cible.longitude))
                except:
                    self.response.write("Prb getG")
            elif cmd == 'setGoalReached':
                try:
                    p = Course.participants[nom]
                    if  p.numCible > 3:
                        Course.vainqueur = p.nom
                        Course.enCours=False
                    else:
                        p.numCible = p.numCible + 1
                        self.response.write(str(p.numCible)+"atteinte")
                except:
                    self.response.write("None")
            elif cmd == 'getWinner':
                try:
                    self.response.write(str(Course.vainqueur))
                except:
                    self.response.write("Prb winner")
        except Exception as e:
            self.response.write(e)


app = webapp2.WSGIApplication([
    ('/', Course)
], debug=True)


