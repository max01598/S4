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

goal
clearwindow,
findAll(X, distanceAvion(X,_),L),
write(L),
affichageVille(L),
tailleListe(L,R),
write(R).
%findAll(X, DistanceAvion(X,_),L)
