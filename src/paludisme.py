from random import randrange
from numpy import array
# Tous les nombres qu'on va citer sont en pourcentage (%)
n = 99#n est l'indice maximale de la matrice, colonne ou ligne(c'est une matrice carrée)

nb_initial_contamine = 20

pourcent_contamination = 25

nb_enfant_moins5ans = 15
pourcent_moins5ans_deces = 61

nb_enfant_plus5ans = 27
pourcent_plus5ans_deces = 65

nb_hommes = 29
pourcent_hommes_deces = 35

nb_femmes = 14.9
pourcent_femmes_deces = 50

nb_femmes_enceinte = 14.9
pourcent_femmes_enceintes_deces = 40

#pour les femmes enceintes, le mieux qu'on a pu faire c’est de trouver plusieurs sources sur le taux de fécondité au Nigeria: en moyenne entre 5 et 6 enfants par femmes au Nigeria donc ca me paraît pas gros de dire que 50 % des femmes (entre 15 et 45 ans donc a peu près 0.5 * 20-25% de la population) au Nigeria sont enceintes.

def init_contamine(contamine):
    a = randrange(1,99)
    if (a <=  contamine):
        malade = 'i'
    else:
        malade = ''
    return malade

#Init_contamine: En fonction du pourcentage du nombre initial de contamination, la fonction retourne ‘i’ si l’individu est infecté, ‘’ sinon. EXEMPLE : si le nombre initial de contamination est de 20, si le chiffre choisis au hasard est entre 1 et 20, il est contaminé, sinon il ne l’est pas. Comme cela, on obtient bien 20% de chance de contamination.

def init_individus():
    a = randrange(1,100)
    if (a <= 25):
        return 4
    elif (a <= 71):
        return 3
    elif (a <= 85):
        return 1
    elif (a <= 90):
        return 2
    else :
        return 0
    
#Init_individus : Avec la même méthode que précédemment, on choisit l’individu au hasard en fonction des variables initialisées au début.

def generate_world():

    individus = (0,'',0)#type_individu,infecté ou gueri,nb semaine contaminé
    world_final = []
    world=[]
    k = 0
    for i in range(0,n+1):
        world = []

        j = 0
        for j in range(0,n+1):
            ind,malade,nb = individus
            ind = init_individus()

            malade = init_contamine(nb_initial_contamine)
            world.append((ind,malade,nb))
            k = k + 1


        world_final.append(world)
    return (world_final)

#Generate_world : Permet de générer un une matrice de taille carré de taille n*1 d’individus. Grâce aux fonctions précédentes, on initialise le type d’individu (hommes, femmes …) et s’il est contaminé.

def voisins(x,y,world):
    tab_voisins = []
    if (y == 0):
        if(x==0):
            tab_voisins.append((0,1))
            tab_voisins.append((1,0))
            tab_voisins.append((1,1))
        elif(x ==n):
            tab_voisins.append((n-1,0))
            tab_voisins.append((n-1,1))
            tab_voisins.append((n,1))
        else:
            tab_voisins.append((x-1,y))
            tab_voisins.append((x-1,y+1))
            tab_voisins.append((x,y+1))
            tab_voisins.append((x+1,y+1))
            tab_voisins.append((x+1,y))


    elif(y == n):
        if (x == n):
            tab_voisins.append((n,n-1))
            tab_voisins.append((n-1,n-1))
            tab_voisins.append((n-1,n))
        elif(x == 0):
            tab_voisins.append((0,n-1))
            tab_voisins.append((1,n-1))
            tab_voisins.append((1,n))
        else :
            tab_voisins.append((x-1,y))
            tab_voisins.append((x-1,y-1))
            tab_voisins.append((x,y-1))
            tab_voisins.append((x+1,y-1))
            tab_voisins.append((x+1,y))


    elif (x == 0):
        tab_voisins.append((x,y-1))
        tab_voisins.append((x+1,y-1))
        tab_voisins.append((x+1,y))
        tab_voisins.append((x+1,y+1))
        tab_voisins.append((x,y+1))

    elif (x == n):
        tab_voisins.append((x,y-1))
        tab_voisins.append((x-1,y-1))
        tab_voisins.append((x-1,y))
        tab_voisins.append((x-1,y+1))
        tab_voisins.append((x,y+1))


    else:

        tab_voisins.append((x-1,y))
        tab_voisins.append((x-1,y-1))
        tab_voisins.append((x,y-1))
        tab_voisins.append((x+1,y-1))
        tab_voisins.append((x+1,y))
        tab_voisins.append((x+1,y+1))
        tab_voisins.append((x,y+1))
        tab_voisins.append((x-1,y+1))


    return tab_voisins

#Voisins : Retourne les coordonnées de tous les voisins d’un individu précis dans la matrice sous forme de liste. Dans ce programme, nous avons supposé que les voisins de l’individu sont ceux situés à une case près de lui, diagonale comprise.


def contamination(x,y,world):
    world2 = world
    tab_voisins = voisins(x,y,world2)
    a,infecte,b = world2[y][x]
    if (infecte == 'i'):
        for voisin in tab_voisins:
            cont = randrange(1,100)

            if (cont <= pourcent_contamination):

                i,j = voisin

                ind,malade,nb = world2[j][i]


                if (malade != 'i' and malade !='g'and malade != 'mort'  and nb <= 5):



                    world2[j][i] = ind,'ai',nb



    return world2

#Contamination : En fonction d’un individu précis dans la matrice, la fonction vérifie si l’individu est contaminé, s’il l’est il va déterminer s’il va contaminer ses voisins (grâce à la fonction voisin) avec pourcent_contamination comme chance de contamination. Les voisins contaminés ont donc leur variable d’infection qui vaut ‘ai’ (Important pour la fonction, comme ça si elle tombe sur un individu ‘ai’ elle ne testera pas sa contamination, car il vient d’être contaminé).

def tour_conta(world):
    world2 = world


    for i in range(0,n+1):
        for j in range(0,n+1):
            world2 = contamination(i,j,world2)
    return world2

#Tour_conta : Permet d’exécuter la fonction Contamination sur toute la matrice (sur chaque individus)

def temps_conta(world):
    world2 = world

    for i in range(0,n+1):
        for j in range(0,n+1):

            a,inf,nb = world2[j][i]
            if (inf == 'ai'):
                inf = 'i'
            elif (inf == 'i'):
                nb = nb + 1
            world2[j][i] = a,inf,nb

    return world2

#Temps_conta : Change les infections de type ‘ai’ en ‘i’

def guerison(world):

    world2 = world

    for i in range(0,n+1):
        for j in range(0,n+1):
             a,inf,nb = world2[j][i]

             if (inf == 'i' and nb >=4):
                inf = 'gueri'

                world2[j][i] = a,inf,nb

    return world2

#Guérison : Si l’individu est infecté depuis plus de 5 semaines, il passe de ‘i’ à ‘guéri’.

def mortalite(world):

    world2 = world
    for i in range(0,n+1):
        for j in range(0,n+1):
            individu,inf,nb = world2[j][i]
            if (inf == 'i'):
                mort = randrange(1,100)
                if (mort <= pourcent_moins5ans_deces/(nb+1) and individu == 4 ):
                    inf = 'mort'
                    nb = 0
                elif (mort <= pourcent_plus5ans_deces/(nb+1) and individu == 3 ):
                    inf = 'mort'
                    nb = 0
                elif (mort <= pourcent_femmes_deces/(nb+1) and individu == 0 ):
                    inf = 'mort'
                    nb = 0
                elif (mort <= pourcent_femmes_enceintes_deces/(nb+1) and individu == 2 ):
                    inf = 'mort'
                    nb = 0
                elif (mort <= pourcent_hommes_deces/(nb+1) and individu == 1 ):
                    inf = 'mort'
                    nb = 0
                else :
                    nb = nb + 1
                world2[j][i] = individu,inf,nb

    return world2

#mortalité : Prends chaque individu, détermine en fonction de son pourcentage de chance de décès s’il meurt. Le pourcentage de chance de décès diminue en fonction des semaines.

def paludisme(world):

    world2 = world
    world2 = tour_conta(world2)
    world2 = temps_conta(world2)
    world2 = mortalite(world2)
    world2 = guerison(world2)


    return world2

#Paludisme : Fait un tour de la matrice et simule le cas du paludisme grâce aux fonctions crées précédemment.

def fin_paludisme(world):

    fin = True
    for i in range(0,n+1):
        for j in range(0,n+1):
            a,inf,b = world[j][i]
            if (inf == 'i'):
                fin = False
    return fin

#Fin_paludisme : Renvoie True si il reste un individu infecté, False sinon.

def tour_paludisme(world):#FONCTION PRINCIPALE : ENTREZ tour_paludisme(generate_world)
    i =0
    world2 = world

    while(fin_paludisme(world2) == False):

        world2 = paludisme(world2)
        i = i + 1
    return (world2)

#Tour_paludisme : Effectue paludisme tant qu’il reste au moins un individu infecté

#--------------------------------------------------------------------------------#
import matplotlib.pyplot as plt
def tracer_temps(repetition):#trace une courbe qui montre le nombre de semaines pour arriver à la fin d'une simulation

    X = []
    Y = []

    repete = 0
    while(repete<repetition):
        i = 0
        world = generate_world()
        while(fin_paludisme(world) == False):

            world = paludisme(world)
            i = i + 1

        Y.append(i)
        X.append(repete)
        repete = repete + 1

    plt.plot(X,Y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    
#Trace une courbe du nombre de semaines qu’il a fallu pour que la maladie disparaisse. On répète cela un nombre « répétition » de fois, l’abscisse correspond donc au numéro de l’essai.

def compter_mort_guersion_infecte(world):
    mort = 0
    gueri = 0
    infecte = 0
    for i in range(0,n+1):
        for j in range(0,n+1):
            a,inf,nb =world[j][i]
            if (inf == 'mort'):
                mort = mort +1
            elif(inf == 'i'):
                infecte = infecte + 1
            elif(inf == 'gueri'):
                gueri = gueri + 1

    return (mort,gueri,infecte)


def tracer_mort_guerison_infecte(world):
    world2 = world
    tab_mort = [0]
    tab_gueri = [0]
    tab_inf = []
    a,b,inf =compter_mort_guersion_infecte(world)
    tab_inf.append(inf)
    temps = [0]
    j = 0
    while(fin_paludisme(world2) == False):

            world = paludisme(world)
            m,g,i = compter_mort_guersion_infecte(world2)
            tab_mort.append(m)
            tab_gueri.append(g)
            tab_inf.append(i)
            j = j +1
            temps.append(j)
    plt.plot(temps,tab_mort,label = "MORT")
    plt.plot(temps,tab_gueri,label = "GUERI")
    plt.plot(temps,tab_inf,label = "INFECTE")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()
    
#Tracer_mort_guerison_infecte(world): Trace le nombre de mort, guéris et infectés en fonction de la semaine.

    




