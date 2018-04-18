# -*- coding: latin-1 -*-

# importation de la librairie graphique
import wxRUR
import math

# Classe de l'application Pacman
class AppPacman(wxRUR.Application) :
    def __init__(self) :
        # Initialise l'application graphique (appel au constructeur parent)
        app = wxRUR.Application.__init__(self,title="Jeu pacman MD", world="pacman.wld")
        self.les_robots = []
        self.numero_robot = 0
        self.les_robots.append(wxRUR.Robot(self, col=1, row=1, orient='E', name="pacman", colour="light blue"))
        self.les_robots.append(wxRUR.Robot(self, col=10, row=1, orient='W', name="pacman", colour="blue"))
        self.les_robots.append(wxRUR.Robot(self, col=1, row=10, orient='E', name="pacman", colour="purple"))
        self.les_robots.append(wxRUR.Robot(self, col=10, row=10, orient='W', name="pacman", colour="green"))
        self.les_robots.append(wxRUR.Robot(self, col=1, row=6, orient='E', name="pacman", colour="grey"))
        # Crée un attribut pacman en position (6,6) tourné vers l'est
        self.pacman = wxRUR.Robot(self, col=6, row=6, orient='E', name="pacman", colour="pacman")
        self.pacman.cases_parcourues = []
        self.pacman.cases_parcourues.append(self.pacman.getPos())
        self.pacman.set_trace_style(style=-1,colour='black')
        self.deplacement = {'E': (1,0) ,'W':(-1,0) ,'S':(0,-1) ,'N':(0,1)}
        #Demande de la vitesse du jeu

        self.vitesse = self.InputInt(text="Entrer la vitesse de la partie : ( Entier entre 1 et 9)", title = "Vitesse des robots")
        while self.vitesse not in range(1,10):
            self.vitesse = self.InputInt(text = "Entrer la vitesse de la partie : ( Entier entre 1 et 9)", title = "Vitesse des robots")
        self.vitesseR = 1.0/self.vitesse
        self.duree = self.InputInt(text ="Entrer la duree limite de la partie : ( Entier entre 30 a 240)", title = "Duree de la partie")
        while self.duree not in range(5,241):
            self.duree = self.InputInt(text = "Entrer la duree limite de la partie : ( Entier entre 30 a 240)", title = "Duree de la partie")
        self.TempEcoule = 0
        self.scr = 0
        # Association de la méthode 'deplacer_pacman'
        # à l'évènement "KeyEvent" (appui sur une touche)
        self.KeyEventHandler(onKeyEvent=self.deplacer_pacman)
        self.TimerEventHandler(onTimerEvent=self.deplacer_un_robot, TimerPeriod = self.vitesseR)
        self.TimerEventHandler(onTimerEvent=self.score, TimerPeriod= 1)

        # Boucle de gestion des évènements de l'application
        self.MainLoop( duration =  self.duree  )
        # Fermeture de l'application
        self.Quit()

    # Méthode évènementielle de déplacement du pacman
    def deplacer_pacman(self, KeyEvent):
        if(len(self.pacman.cases_parcourues)==100):
            wxRUR.Application.ShowMessage(self, text="Gagne !!! Tu as toutes les cases "+ " Nb cases parcourues : "+ str(len(self.pacman.cases_parcourues)) + " Score : " + str(self.scr), title="fin de la partie")
            wxRUR.Application.ExitMainLoop(self)
        else:
            directionsPossible = {315:'N',314:'W',317:'S',316:'E'}
            direction = KeyEvent.GetKeyCode()
            if(directionsPossible.has_key(direction)):
                direction = directionsPossible[direction]
                if(self.pacman.is_clear(direction)):
                    self.pacman.turn(direction)
                    self.pacman.move()
                    if(self.pacman.cases_parcourues.count(self.pacman.getPos())==0):
                        self.pacman.cases_parcourues.append(self.pacman.getPos())
                    for robot in self.les_robots:
                        if robot.getPos() == self.pacman.getPos() :
                            if len(self.pacman.cases_parcourues)!=100 :
                                wxRUR.Application.ShowMessage(self, text="Perdu !!! Tu a rencontre un robot" + " Nb cases parcourues : "+ str(len(self.pacman.cases_parcourues)) + " Score : " + str(self.scr), title="fin de la partie")
                                wxRUR.Application.ExitMainLoop(self)
        pass

    def distance_au_pacman(self,robot,direction):
        xp,yp = self.pacman.getPos()
        xr,yr = robot.getPos()
        coordonnex,coordonney = self.deplacement[direction]
        newxr,newyr = xr+coordonnex, yr+coordonney
        distance = math.sqrt((xp-newxr)*(xp-newxr)+(yp-newyr)*(yp-newyr))
        return distance


    def direction_poursuite(self,robot):
        distanceMax = 0
        bestDirection = None
        for direction in self.deplacement.keys() :
            if robot.is_clear(direction) :
                distanceTest = self.distance_au_pacman(robot, direction)
                if distanceTest < distanceMax or bestDirection == None:
                    distanceMax = distanceTest
                    bestDirection = direction
        return bestDirection

    def deplacer_un_robot(self,TimerEvent):
        direction = self.direction_poursuite(self.les_robots[self.numero_robot])
        self.les_robots[self.numero_robot].turn(direction)
        self.les_robots[self.numero_robot].move()
        if self.pacman.getPos() == self.les_robots[self.numero_robot].getPos() :
            wxRUR.Application.ShowMessage(self, text="Game over : Les robots ont eu raison de vous !!!" + " Nb cases parcourues : "+ str(len(self.pacman.cases_parcourues)) + " Score : " + str(self.scr), title="fin de la partie")
            wxRUR.Application.ExitMainLoop(self)
        self.numero_robot = (self.numero_robot+1)%len(self.les_robots)




    def score(self,TimerEvent):
        temps = self.duree - self.TempEcoule
        self.TempEcoule += 1
        self.scr =  3*self.vitesse*len(self.pacman.cases_parcourues)
        self.SetStatusText("Temps restant : " + str(temps-1) + " Nb cases parcourues : " + str(len(self.pacman.cases_parcourues) ) + " score : " + str(self.scr) )
        print (self.TempEcoule)
        print (self.duree)
        if(self.TempEcoule == self.duree-1):
            print(self.TempEcoule)
            wxRUR.Application.ShowMessage(self, text="Game over : Le temps a eu raison de vous "+ " Nb cases parcourues : "+ str(len(self.pacman.cases_parcourues)) + " Score : " + str(self.scr), title="fin de la partie")


# Crée une instance de l'application Pacman

appPacman = AppPacman()