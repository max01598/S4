predicates
ValeurFactoriel(integer,integer)
%ValeurFactoriel(3,X) renvoie X la factorielle de 3 soit (3*2*1) 6.

clauses
ValeurFactoriel(0,1).
ValeurFactoriel(1,1).
ValeurFactoriel(X, Result):- X > 1, X1 = X-1, ValeurFactoriel(X1, Result1), Result = Result1 * X.


goal
clearwindow,
write("Nombre ?"),
nl,readint(Str1),
ValeurFactoriel(Str1,X),
write("Resultat: ",X).