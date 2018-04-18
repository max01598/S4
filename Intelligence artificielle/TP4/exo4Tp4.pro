domains
	ville = symbol
	distance = integer
	listeV = ville*
	
predicates
distanceTrain(ville,distance).
%DistanceTrain(bruxelles, 1000) signifie que la distance en train entre Toulouse et Bruxelles est de 1000
distanceAvion(ville,distance).
%DistanceAvion(rome, 1500) signifie que la distance en avion entre Toulouse et Rome est de 1500
affichageVille(listeV).
tailleListe(listeV,integer).
concatenerListe(listeV,listeV,listeV).
contient(listeV,ville).
chercherSiDesservie(listeV,listeV,ville).



clauses
distanceTrain(bruxelles,1000).
distanceTrain(barcelone,500).
distanceTrain(milan,1000).
distanceTrain(paris,800).
distanceAvion(rome,1500).
distanceAvion(londres,1000).
distanceAvion(tunis,2000).
affichageVille([]).
affichageVille([V|Q]):-write(V," "), affichageVille(Q).
tailleListe([],0).
tailleListe([_|Y],L):-tailleListe(Y,L2), L = L2+1.
concatenerListe([],L,L).
concatenerListe([X|Y],L,[X|R]):-concatenerListe(Y,L,R).
contient([V|_],X):-T=X.
contient([V|Q],X):-V<>X,contient(Q,X).
chercherSiDesservie(L1,_,X):-contient(L1,X),write(X," est desservie en train"), fail.
chercherSiDesservie(_,L2,X):-contient(L2,X),write(X," est desservie en avion").
chercherSiDesservie(L1,L2,X):-contient(L1,X),contient(L2,X),write(X," est desservie en avion et en train").
chercherSiDesservie(L1,L2,X):-not(contient(L1,X)),not(contient(L2,X)),write(X," n'est pas desservie").

goal
clearwindow,
write("Ville :"),
readln(str1),
findAll(X, distanceAvion(X,_),L),
findAll(X2, distanceTrain(X2,_),L2),
chercherSiDesservie(L,L2,str1).




%findAll(X, DistanceAvion(X,_),L)
%chercherSiDesservie([],[],X).
%chercherSiDesservie([V|Q],_,X):-X=V,write(X," est desservie en train").
%chercherSiDesservie([V|Q],_,X):-chercherSiDesservie(Q,_,X).
%chercherSiDesservie(_,[V|Q],X):-X=V,write(X," est desservie en avion").
%chercherSiDesservie(_,[V|Q],X):-chercherSiDesservie(_Q,X).