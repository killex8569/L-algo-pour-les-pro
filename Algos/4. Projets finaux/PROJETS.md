# introduction

L'objectif de cette partie est de compiler les éléments que vous avez après juste avant, l'idée est de mettre en place. 
Ce document vous donne des idées de projets de "fin d'apprentissage". En théorie, à la fin de ces exercices, 
si vous n'avez pas utilisé ni l'ia, ni internet (sauf blocages vraiment important), dans ce cas, vous devriez être pro.

Je vous conseille de regarder cette vidéo du youtubeur "Ego" juste avant, il explique et explore vraiment en profondeur le thème ou alors la page Wikipédia qui est vraiment complète : 

- [Wikipédia](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)
- [Ego - Le jeu de la vie](https://www.youtube.com/watch?v=eMn43As24Bo&t=626s&pp=ygUUZWdvIGxlIGpldSBkZSBsYSB2aWU%3D)


## Jeu de la vie (de Conway)

Le jeu de la Vie est un « jeu à zéro joueur », c'est-à-dire qu'il ne nécessite aucune intervention du joueur lors de son déroulement, le jeu de la vie à été "inventé" par John Conway en 1970. 
L'objectif est de simuler la vie


Règles du jeu de la vie : 

- Une cellule morte (0) possédant exactement 3 voisines devient vivante.
- Une cellule vivante ne possédant pas exactement, deux ou trois cellules vivantes deviennent mortes.

À chaque "tour" (donc si l'on décide qu'une case devient morte ou vivante), est appeler **une génération**


### Configuration du jeu de la vie de Conway

Grâce à ces propriétés, le jeu de la vie de Conway nous permet de découvrir des "Amas de cellule vivante", des groupes de cellules qui peuvent se déplacer, générer de nouveau groupes de cellules (des géniteurs), des groupes laissant des déchets sur leurs passages, etc...

Voici une liste des **structures** que l'on peut retrouver : 
- Structures stables --> ensembles de cellules ayant stoppé toute évolution 
- Oscillateurs --> Les oscillateurs se transforment de manière cyclique, en revêtant plusieurs formes différentes avant de retrouver leur état initial (blinker par exemple)
- Vaisseaux --> structures capables, après un certain nombre de générations, de produire une copie d’elles-mêmes, mais décalées dans l’univers du jeu
- Mathusalems --> Les mathusalems sont des structures actives qui mettent un certain temps avant de se stabiliser (souvent plusieurs milliers de générations).
- Puffeurs --> configurations qui se déplacent en laissant derrière elles une traînée constituée de débris
- Canons --> configurations qui émettent un autre motif, tel qu'un vaisseau, à intervalles réguliers (aussi nommé "géniteur")
- Jardin d'Éden --> configuration sans passé possible : aucune configuration ne donne à l’étape suivante un Jardin d’Éden.


Ce jeu est **turring complet** : 
Malgré sa simplicité, ce jeu est une machine de Turing universelle : il est possible de calculer tout algorithme pourvu que la grille soit suffisamment grande et les conditions initiales correctes.


## Le labyrinthe

L'objectif est de générer un labyrinthe de manière aléatoire (On pourras y définir des paramètres tels que la taille de ce labyrinthe, si il est carré ou rectangulaire etc.)

L'objectif est au final, de générer un labyrinthe complet et unique de taille définis, puis de trouver la sortie(trouver un chemin qui mène à une sortie)
