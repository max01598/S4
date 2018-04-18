predicates
prixLogementUneSemaine(symbol,symbol,integer)
%prixLogementUneSemaine(londres,hotel,2300) signifie que le prix d'un sejour d'une semaine dans un hotel à londres
prixTransport(symbol,symbol,integer)
%prixTransport(londres,avion,1500) signifie que le prix d'un voyage à destination de londres est 1500
prixSejour(symbol,symbol,symbol,integer,integer)
% prixSejour(rome, camping, avion, 2, X) signifie que 
% le prix de 2 semaines en camping en y allant en avion
% sera de X
avion(symbol, integer)
% avion(londres, 1000) signifie que 
% le prix de du voyage pour aller a londres en 
% avion est de 1000
	
ferry(symbol, integer)
% ferry(londres, 1000) signifie que 
% le prix de du voyage pour aller a londres en 
% ferry est de 1000
	
hotel(symbol, integer)
% hotel(londres, 1000) signifie que 
% le prix de du logement en hotel a londres en 
% est de 1000
	
chambre(symbol, integer)
% chambre(londres, 1000) signifie que 
% le prix de du logement en chambre a londres en 
% est de 1000
	
camping(symbol, integer)
% camping(londres, 1000) signifie que 
% le prix de du logement en camping a londres en 
% est de 1000


clauses
avion(londres,1500).
avion(rome,1000).
avion(tunis,2000).
ferry(londres,800).
ferry(tunis,1200).
hotel(londres,2300).
hotel(rome,2100).
hotel(tunis,3000).
chambre(londres,1450).
chambre(rome,1050).
chambre(tunis,900).
camping(londres,840).
camping(rome,700).
camping(tunis,500).
prixTransport(X,avion,P):-avion(X,P).
prixTransport(X,ferry,P):-ferry(X,P).
prixLogementUneSemaine(X,hotel,P):-hotel(X,P).
prixLogementUneSemaine(X,chambre,P):-chambre(X,P).
prixLogementUneSemaine(X,camping,P):-camping(X,P).
prixSejour(V,L,T,S,P):-prixLogementUneSemaine(V,L,X),prixTransport(V,T,Y),P=S*X+Y.
possible(X,Y,Z):-prixSejour(X,Y,T,Z,P),write("Vous pouvez aller en ",Y," a ",X," en y allant en ", T," pour ",P, " euros"),nl,fail.
possible(X,Y,Z):-not(prixSejour(X,Y,_,Z,_)),write("Désolé ... pas de séjour à ",X," à ",Z).

goal
clearwindow,
write("Destionation :"),
readln(Str1),
write("Durée :"),
nl,readint(Int1),nl,
write("Logement :"),
nl,readln(Str2),
possible(Str1,Str2,Int1).