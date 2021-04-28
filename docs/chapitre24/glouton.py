from itertools import permutations

D = [[0, 55, 303, 188, 183], [55, 0, 306, 176, 203],
     [303, 306, 0, 142, 153], [188, 176, 142, 0, 123],
     [183, 203, 153, 123, 0]]

## ------- exercice 1 --------

def longueur_iti(distances, itineraire):
    """ distances est le tableau des distances entre les villes.
    itinéraire est un tuple qui décrit un itinéraire 
    Renvoie la distance totale parcourue entre les villes en
    suivant l'itinéraire """
    
    dist = 0
    origine = 0
    for destination in itineraire:
        dist += distances[origine][destination]
        origine = destination
    dist += distances[origine][0]
    return dist
    

def dist_opti(distances):
    n = len(distances)
    villes = list(range(1, n))  # liste des villes
    mini = sum(distances[0])
    iti_mini = [tuple(range(1, n))]
    for itineraire in permutations(villes):
        longueur = longueur_iti(distances, itineraire)
        if longueur < mini:
            mini = longueur
            iti_mini = itineraire
    return mini, iti_mini


## ------- exercice 2 --------

def plus_proche(ville, distances, visitees):
    """ ville est un entier qui donne le numéro d'une ville
    distances est le tableau des distances entre les villes.
    visitees est un tableau de booléens qui indique pour chaque
    ville si elle a été visitée
    Renvoie le numéro de la ville la plus proche de ville parmi celle
    qui n'ont pas encore été visitées"""
    
    n = len(distances)
    dist_mini = float('+inf')  # initialise avec une valeur << infinie >> 
    for ville_courante in range(n):
        dist = distances[ville][ville_courante]
        if not(visitees[ville_courante]) and dist < dist_mini:
            dist_mini = dist
            choix = ville_courante
    return choix

def pvc_glouton(distances, depart):
    """ """

    n = len(distances)
    visitees = [False]*n
    dist = 0     
    itineraire = [depart]
    ville = depart
    
    for _ in range(n-1):
        visitees[ville] = True  # marque la ville comme visitée
        suivante = plus_proche(ville, distances, visitees)
        itineraire.append(suivante)
        dist += distances[ville][suivante]
        ville = suivante

    dist += distances[ville][depart]
    
    return dist, itineraire
        
        
## ------- exercice 3 --------

euros = [1, 2, 5, 10, 20, 50, 100, 200]

def nb_rendu(sys, n):
    """ sys est une liste croissante d'entiers qui représente un système monétaire.
    n est entier. Renvoie le nombre de pièces et billets nécessaires pour rendre $n$ euros
    en appliquant l'algorithme glouton"""

    nb_piece = 0
    a_rendre = n
    indice_valeur = len(sys) - 1
    
    while a_rendre > 0:
        if a_rendre >= sys[indice_valeur]:
            nb_piece += 1
            a_rendre -= sys[indice_valeur]
        else:
            indice_valeur += -1

    return nb_piece


def detail_rendu(sys, n):
    """ sys est une liste croissante d'entiers qui représente un système monétaire.
    n est entier. Renvoie le rendu de monnaie pour une valeur n sous la forme d'une
    liste de couples (valeur, effectif) obtenu en appliquant l'algorithme glouton """

    rendu = []
    a_rendre = n
    indice_valeur = len(sys) - 1  # On commence avec la plus grande valeur
    effectif_valeur = 0
    
    while a_rendre > 0:
        if a_rendre >= sys[indice_valeur]:  # La somme à rendre est plus grande que la valeur courante du systeme
            effectif_valeur += 1
            a_rendre -= sys[indice_valeur]
        else:   # La somme à rendre est plus petite que la valeur courante du systeme
            rendu.append((sys[indice_valeur], effectif_valeur))
            indice_valeur += -1
            effectif_valeur = 0

    rendu.append((sys[indice_valeur], effectif_valeur))
    return rendu
