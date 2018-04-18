predicates
homme(symbol)
personne(symbol)
aime(symbol,symbol)
estomacVide(symbol)
aFaim(symbol)
chien(symbol)
chat(symbol)
aimePas(symbol,symbol)
informaticien(symbol)
travail(symbol)
bienPaye(symbol)
agreable(symbol)
exercer(symbol,symbol)
aimeTravail(symbol,symbol)
age(symbol,integer)
plusAge(symbol,symbol)
habite(symbol,symbol)
tel(symbol,string)
seSitue(symbol,symbol)



clauses
homme(bruno). %bruno est un homme
personne(bruno). %bruno est une personne
personne(X) :- homme(X).

aime(bruno,pizza). %bruno aime les pizzas
aime(pierre,velo). %pierre aime le velo
aime(paul,parapente). %paul aime le parapente
aime(bruno,X) :- chien(X).
aime(bruno,X) :- chien(X).
aime(paul,X) :- aime(pierre,X).
aimePas(X,Y) :- chien(X),chat(Y).

estomacVide(bruno). %bruno a l'estomac vide
aFaim(X) :- personne(X),estomacVide(X).

chien(milou). %milou est un chien
chat(zoe). %zoe est un chat
informaticien(bruno). %brun est informaticien
travail(informaticien). %informaticen est un travail
bienPaye(informaticien). %informaticien est bien paye
agreable(informaticien). %informaticien est agreable
exercer(X,Y) :- personne(X), travail(Y).
aimeTravail(X,Y) :- travail(Y),personne(X),exercer(X,Y),bienPaye(Y),agreable(Y).

age(bruno,20). %bruno a 20 ans
age(milou,7). %milou a 7 ans
plusAge(X,Y) :- age(X,X1),age(Y,Y1), X1>Y1.

habite(bruno,dijon). %bruno habite à dijon
tel(pierre,"05.61.23.45.67"). %le tel de pierre est 
seSitue(dijon,france). %dijon se situe en france


%Si qui est une personne et quoi un objet, alors si qui a acheté quoi alors qui possede quoi.
%Si qui est une personne et quoi un objet et si Tiers une personne a donné quoi à qui, alors qui possède quoi.






