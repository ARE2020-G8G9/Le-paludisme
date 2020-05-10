## Travail effectué 

=> Description hebdomadaire du travail effectué 

Tout d'abord, avant de commencer à décrire notre travail hebdomadaire, il faut savoir que vu qu'on est un groupe un peu chargé qui constitue 5 personnes, on a décidé de diviser les taches entres nous afin que chacun puisse faire sa part et parfois nous étions obligé de vous décrire une tache faite à deux voire même à trois, pour cela notre projet a pris à peu près 6 semaines de travail.

   #### J.AOUCHICHE 
### Semaine 1 
#### J.AOUCHICHE
Pour ma part pendant cette première semaine je me suis donné la tache de coordinateur dans le groupe afin que nous nous organisions, en effet au début ça n'a pas été simple, d'abord j'ai essayé d'avoir tout les outils nécessaires qu'il nous faudra pour ce projet à savoir les sites internet, les sources fiables et les applications et logiciel qui nous faudra pour que notre projet fonctionne convenablement, et j'ai du expliquer aux membres du groupe ce qu'il fallait, et la tâche de chacun .

### Semaine 2 
#### S.MUHAMMAD
Pour commencer comme il se doit le projet je me devais de créer le site mais avant bien évidemment j'ai suivi tel un mode d’emploi les deux vidéos explicatifs faites par le prof sur moodle; je me devais donc d'installer l'application git me permettant d'ajouter du contenu sur le site sans avoir à m'y rendre à chaque fois. 

### Semaine 3  Partie variables & constantes
#### A.AISSAOUI & R.TAIBI
Deux semaines plus tard, nous avons décider moi Alexandre et Ramy de nous focaliser sur le code qu'il faut pour notre projet (la simulation du code concerne le Nigeria). 
En même temps nous avions commencer le carnet de bord et la recherche bibliographique, les deux à l'aide des autres membres du groupe, et comme prévu on a essayé de chercher sur internet les différentes constantes et variables que nous trouvions essentielles et importantes pour nos fonctions, et nous allons maintenant expliquer cette partie :

On a supposé que la maladie durait 5 semaines à partir de l’infection.
### EXPLICATION DES CONSTANTES :
n = 99 #n est l'indice maximale de la matrice, colonne ou ligne(c'est une matrice carrée)

nb_initial_contaminé = 20

pourcent_contamination = 50

Au Nigeria, il y a 42% d’enfants entre 0 et 14 ans, 58 % d’adultes. On suppose qu’il y a autant d’hommes que de femmes. Donc on obtient ,29% de femmes et 29% d’hommes.
Pour trouver le nombre d’enfants, on va supposer qu’il y a autant d’enfants de 0 à 1 an que d’enfants de 1 à 2ans que de 2 à 3 ans…
On arrive à un 15% pour les enfants de moins de 5 ans. ((42 / 14) * 5). Donc il reste 27% d’enfants de plus de 5 ans.

nb_enfant_moins5ans = 15

nb_enfant_plus5ans = 27

nb_hommes = 29

nb_femmes = 20

nb_femmes_enceinte = 29

Pour les femmes enceintes, le mieux que nous avions pu faire c’est trouver plusieurs sources sur le taux de fécondité au Nigeria: en moyenne entre 5 et 6 enfants par femmes au Nigeria donc ça nous paraît pas énorme de dire que 50 % des femmes (entre 15 et 45 ans donc a peu près 0.5 * 20-25% de la population) au Nigeria sont enceintes.

pourcent_moins5ans_décès = 65
(Tous les chiffres sont de 2017) : 

-219 000 000 cas dans le monde , 435000 morts dues au paludisme dans le monde (OMS).

-25% des cas au Nigeria (OMS) => 0.25*219000000 = 54 750 000 cas au Nigeria (1)

-19% de ces morts au Nigeria (OMS)  => 0.19 * 435000 = 82650 morts au Nigeria.  


Pour taux de contamination :59 cas de paludisme pour 1000 personnes exposées (parmi les pays touchés dans le monde) (OMS) = 0.059 % de contamination (c’est 5x (4,86 plutôt) plus élevé au Nigeria… 0.059*190 000 000 = 11 269 000 cas théoriques contre (1) )
61% de décès d’enfants de moins de 5 ans ( les plus vulnérables et exposés aux moustiques et les plus touchés) dans le monde (OMS: 266 000 / 435 000 ) => raccourci: 61% des décès au Nigeria sont des enfants -5 ans (au moins, c’est le pays le plus touché!) 

nb_enfant_plus5ans = 46
pourcent_plus5ans_décès = 45

nb_hommes = 14
pourcent_hommes_décès = 35

nb_femmes = 9
pourcent_femmes_décès = 35

nb_femmes_enceinte = 5
pourcent_femmes_enceintes_décès = 65

### Semaine 4
#### M.CHIKH & S.MUHAMMAD & J.AOUCHICHE
Comme on le voit cette partie regroupe 3 membres qui nous a sembler plus dure par rapport aux autres travaux effectuer qui est est celle des "fonctions", nous allons lister les différentes fonctions utilisées tout en expliquant leur fonctionnement:

### EXPLICATION DES FONCTIONS:

Init_contamine:
En fonction du pourcentage du nombre initial de contamination, la fonction retourne ‘i’ si l’individu est infecté, ‘’ sinon. EXEMPLE : si le nombre initial de contamination est de 20, si le chiffre choisis au hasard est entre 1 et 20, il est contaminé, sinon il ne l’est pas. Comme cela, on obtient bien 20% de chance de contamination.

Init_individus : 
Avec la même méthode que précédemment, on choisit l’individu au hasard en fonction des variables initialisées au début.

Generate_world :
Permet de générer un une matrice de taille carré de taille n*1 d’individus. Grâce aux fonctions précédentes, on initialise le type d’individu (hommes, femmes …) et s’il est contaminé.

Voisins :
Retourne les coordonnées de tous les voisins d’un individu précis dans la matrice sous forme de liste. Dans ce programme, nous avons supposé que les voisins de l’individu sont ceux situés à une case près de lui, diagonale comprise.

Contamination :
En fonction d’un individu précis dans la matrice, la fonction vérifie si l’individu est contaminé, s’il l’est il va déterminer s’il va contaminer ses voisins (grâce à la fonction voisin) avec pourcent_contamination comme chance de contamination. Les voisins contaminés ont donc leur variable d’infection qui vaut ‘ai’ (Important pour la fonction, comme ça si elle tombe sur un individu ‘ai’ elle ne testera pas sa contamination, car il vient d’être contaminé).

Tour_conta :
Permet d’exécuter la fonction Contamination sur toute la matrice (sur chaque individus) ;

### Semaine 5 
#### M.CHIKH & S.MUHAMMAD & J.AOUCHICHE
### EXPLICATION DES FONCTIONS (suite):

Nous allons continuer ce qu'on a laissé pour la semaine 4 :
Temps_conta :
Change les infections de type ‘ai’ en ‘i’

Guérison :
Si l’individu est infecté depuis plus de 5 semaines, il passe de ‘i’ à ‘guéri’.

Mortalité :
Prends chaque individu, détermine en fonction de son pourcentage de chance de décès s’il meurt. Le pourcentage de chance de décès diminue en fonction des semaines.

Paludisme :
Fait un tour de la matrice et simule le cas du paludisme grâce aux fonctions crées précédemment.

Fin_paludisme :
Renvoie True si il reste un individu infecté, False sinon.

Tour_paludisme :
Effectue paludisme tant qu’il reste au moins un individu infecté.

Tracer_temps :
Trace une courbe du nombre de semaines qu’il a fallu pour que la maladie disparaisse. On répète cela un nombre « répétition » de fois, l’abscisse correspond donc au numéro de l’essai.

Tracer_mort_guerison_infecte(world):
Trace le nombre de mort, guéris et infectés en fonction de la semaine.
## comme ça on a fini d'expliquer la partie "FONCTIONS" !!!

### Après avoir fini le carnet de Bord ,nous l'avons envoyé un jour après le delai qui est le 1 mai car nous avons cru que c'était avant le 10 mai.  

### Semaine 6:
### S.MUHAMMAD & J.AOUCHICHE
Pour cette semaine nous avons rempli le site, plus exactement la partie présentation du projet qui est "paludisme".
De plus nous nous devions de suivre d'autres tutoriel que celle fournie par le professeur, afin de pouvoir ajouter des iamges plus tard pour notre site, ce qui semble être simple mais nous a pris une grosse heure juste pour la compréhension de la procédure à effectuer.

### R.TAIBI & A.AISSAOUI
Nous avons rempli la partie bibliographie du site, et nous avons aussi dessiner la carte mentale composer de nos mots_clés qui nous ont permis d'effectuer nos recherches et d'avoir toutes les informations nécessaires.

### M.CHIKH 
J'ai rempli la fiche synthétique tout en respectant le rendu qu'on nous a remis et j'ai fais la partie résultats et l’analyse critique.


# THE END 
### ...
<a href="index.html"> Retour à la page principale </a>
