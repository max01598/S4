predicates
prixLogementUneSemaine(symbol,symbol,integer)
%prixLogementUneSemaine(londres,hotel,2300) signifie que le prix d'un sejour d'une semaine dans un hotel à londres
prixTransport(symbol,symbol,integer)
%prixTransport(londres,avion,1500) signifie que le prix d'un voyage à destination de londres est 1500
prixSejour(symbol,symbol,symbol,integer,integer)
% prixSejour(rome, camping, avion, 2, X) signifie que 
% le prix de 2 semaines en camping en y allant en avion
% sera de X


clauses
prixTransport(londres,avion,1500).
prixTransport(rome,avion,1000).
prixTransport(tunis,avion,2000).
prixTransport(londres,ferry,800).
prixTransport(tunis,ferry,1200).
prixLogementUneSemaine(londres,hotel,2300).
prixLogementUneSemaine(londres,chambre,1450).
prixLogementUneSemaine(londres,camping,840).
prixLogementUneSemaine(rome,hotel,2100).
prixLogementUneSemaine(rome,chambre,1050).
prixLogementUneSemaine(rome,camping,700).
prixLogementUneSemaine(tunis,hotel,3000).
prixLogementUneSemaine(tunis,chambre,900).
prixLogementUneSemaine(tunis,camping,500).
prixSejour(V,L,T,S,P):-prixLogementUneSemaine(V,L,X),prixTransport(V,T,Y),P=S*X+Y.