domains
	nom = symbol
	nbSelection = integer
	postePossible = symbol
	listeJ = nom*

predicates
	joueur(nom,nbSelection)
	poste(nom,postePossible)
	affichageDetail(nom)
	listeJparPoste(postePossible)
	affichageListeJ(listeJ)
	listeMc(listeJ)
	listeMd(listeJ)
	listeMg(listeJ)
	concatenerListe(listeJ,listeJ,listeJ)
	contenir(listeJ,nom)
	test(listeJ,nom)
	calculSomme(listeJ,integer)
	tailleListe(listeJ,integer)
	calculMoy(integer,integer,integer)

clauses
	joueur(henry,8).
	joueur(trezeguet,5).
	joueur(blanc,9).
	joueur(thuram,6).
	joueur(desailly,8).
	joueur(djorkaeff,10).
	joueur(lizarazu,10).
	poste(henry,avg).
	poste(henry,avd).
	poste(trezeguet,avc).
	poste(trezeguet,avd).
	poste(blanc,arc).
	poste(thuram,ard).
	poste(desailly,mg).
	poste(desailly,mc).
	poste(desailly,md).
	poste(djorkaeff,mc).
	poste(djorkaeff,md).
	poste(lizarezu,arg).
	poste(lizarezu,arm).
	affichageDetail(N):-not(joueur(N,S)),write("Joueur inconnu").
	affichageDetail(N):-joueur(N,S),poste(N,P),write("Joueur :", N,nl,"Nombre de selection :", S,nl,"Poste :", P,nl).
	%listeJparPoste(P,L):-findAll(X,poste(X,P),L),affichageListeJ(L).
	listeJparPoste(P,L):-findAll(X,poste(X,P),L).
	affichageListeJ([T]):-write(" Joueur : ", T),nl.
	affichageListeJ([T|Q]):-write(" Joueur : ", T),nl,affichageListeJ(Q).
	listeMc(L):-findAll(X,poste(X,mc),L).
	listeMd(L):-findAll(X,poste(X,md),L).
	listeMg(L):-findAll(X,poste(X,mg),L).
	concatenerListe([],L,L).
	concatenerListe([X|Y],L,[X|R]):-concatenerListe(Y,L,R).
	contenir([T|Q],X):-T<>Q, contenir(Q,X).
	contenir([T|_],X):-T=X.
	test(L,X):-not(contenir(L,X)),write( X , " n'est pas un milieu"),nl.
	test(L,X):-contenir(L,X),write( X , " est un milieu"),nl.
	calculSomme([],0).
	calculSomme([T|Q],R):-joueur(T,S),calculSomme(Q,R2), R = R2 + S.
	tailleListe([],0).
	tailleListe([_|Y],L):-tailleListe(Y,L2), L = L2+1.
	calculMoy(X,Y,M):-M=X/Y. 

goal
clearwindows,
write("Entrer le nom d'un joueur :"),nl,
realln(Nom),
affichageDetail(Nom),nl,
write("Entrer le poste :"),
readln(Poste),
listeJparPoste(Poste,L),
affichageListeJ(L),
listeMc(Lc),
listeMd(Ld),
listeMg(Lg),
ConcatenerListe(Ld,Lc,Ldc),
ConcatenerListe(Ldc,Lg,Lt),
affichageListeJ(Lt),
write("Entrer le nom d'un joueur :"),nl,
realln(Nom2),
test(Lt,Nom2),
findAll(X,joueur(X,_),L1),
calculSomme(L1,Somme),
tailleListe(L1,Taille),
calculMoy(Somme,Taille,Moyenne),
write("Moyenne : ", Moyenne).
