predicates
destination(symbol)
%destination(londres) signifie que londres est une destination
modeLogement(symbol)
%logement(hotel) signifie qu'un hotel est un mode de logement 
transport(symbol)
%transport(avion) signifie que l'avion est un mode de transport
prixLogementUneSemaine(symbol,symbol,integer)
%prixLogementUneSemaine(londres,hotel,2300) signifie que le prix d'un sejour d'une semaine dans un hotel à londres
prixTransport(symbol,symbol,integer)
%prixTransport(londres,avion,1500) signifie que le prix d'un voyage à destination de londres est 1500

clauses
destination(londres).%londres est une destination
destination(rome).%rome est une destination
destination(tunis).%tunis est une destination
modeLogement(hotel).%hotel est un mode de logement
modeLogement(chambre).%chambre est un mode de logement
modeLogement(camping).%camping est un mode de logement
transport(avion).%avion est un mode de transport
transport(ferry).%ferry est un mode de transport
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