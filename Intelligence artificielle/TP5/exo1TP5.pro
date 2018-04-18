domains
	couleur = symbol
	titre = symbol
	auteur = symbol
	theme = symbol
	prix = integer
	listeT = titre*
	listeA = auteur*

predicates
livre(couleur,titre,auteur)
%
caracteristique(couleur,theme,prix)
%
affichagelisteAvecPrix(auteur)
%
contenir(listA,auteur)
%
listeNoire()
%
listeRose()
%
listeVerte()
%
affichageListe(listeA,couleur)
%
testPlusieursCouleur(auteur)
%

affichageNbLivreParCouleur(auteur,couleur)
%

calculNbLivre(listeL,integer)
%

clauses
livre(noire,maitre_illusions,tart).
livre(verte,tour_sombre,king).
livre(rose,goeland,back).
livre(verte,thanatonautes,werber).
livre(verte,farenheit,bradbury).
caracteristique(noire,policier,15).
caracteristique(rose,roman,17).
caracteristique(verte,fiction,20).
affichagelisteAvecPrix(X):-not(livre(_,_,X)),write("Auteur non repertorie"),nl.
affichagelisteAvecPrix(X):-livre(C,T,X),caracteristique(C,_,P),write(" ",T," prix : ",P),nl.
contenir([],T).
contenir([V|Q],T):-V<>T,contenir(Q,T).
AffichageListe([],_).
AffichageListe([T|Q],_):-write(" ",T),AffichageListe(Q,_).
AffichageListe([T|Q],C):-write(C," Auteur :",T),AffichageListe(Q,_).
listeNoire():-findAll(A,livre(noire,_,A),L), AffichageListe(L,noire).
listeRose():-findAll(A,livre(rose,_,A),L), AffichageListe(L,rose).
listeVerte():-findAll(A,livre(verte,_,A),L), AffichageListe(L,verte).
TestPlusieursCouleur(A):-findAll(A,livre(noire,_,A),L1),findAll(A,livre(rose,_,A),L2),findAll(A,livre(verte,_,A),L3),
contenir(L1,A)/\contenir(L2,A)\/contenir(L1,A)/\contenir(L3,A)\/contenir(L2,A)/\contenir(L3,A),write("Auteur dans plusieur cat").
calculNbLivre([],0).
calculNbLivre([_|Q],R):-calculNbLivre([_|Q],R2), R = R2 + 1
AffichageNbLivreParCouleur(A,C):-findAll(T,livre(C,T,A),L),calculNbLivre(L,R),write("nb livre :",R).





goals
clearwindow,
write("Nom de l'auteur :"),
readln(str1),
findall(str1,livre(_,X,str1),L),
write(L),
affichagelisteAvecPrix(L),
listeNoire(),
listeRose(),
listeVerte(),
TestPlusieursCouleur(str1).




