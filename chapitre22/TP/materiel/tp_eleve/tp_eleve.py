#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP KNN eleve
"""

from utilitaires_knn import *
import math
import random

#%% Partie 1 : implémentation


def distance_euclidienne(enreg_a, enreg_b, tab_descripteur):
    """
    Parameters
    ----------
        enreg_a, enreg_b et deux enregistrements de données sous forme de 
        dictionnaires
        tab_descripteur un tableau de descripteurs (certaines clefs des 
                                                    enregistrements)
    
    Returns
    -------
        distance euclidienne entre enreg_a et enreg_b selon les valeurs des 
        descripteurs de tab_descripteur arrondie à 3 chiffres après la virgule
    """
    distance_carre = 0
    for descripteur in tab_descripteur:
        "à compléter "
        
        
        
    return round(math.sqrt(distance_carre), 3)


def table_distance_nouveau(table, nouveau, distance, etiquette, tab_descripteur):
    """
    Parameters
    ----------
    table : une table d'enregistrements de type dictionnaire
    nouveau : un nouvel enregistrement de type dictionnaire
    distance : une fonction de distance entre deux enregistrements
    etiquette : nom du descripteur d'étiquette dans les enregistrements
    tab_descripteur : un tableau avec les noms des descripteurs utilisés
    dans le calcul de la distance
    
    Returns
    -------
    tab_distance un tableau de tuple (distance entre nouveau et un 
    enregistrement de table, étiquette de cet enregistrement)
    """    
    tab_distance = []
    for enreg in table:
        "à compléter "
        
       
    return tab_distance

def clef_tri(couple):
    """Clef de tri pour trier un couple de valeurs selon
    la première composante"""
    return couple[0]


def trier_puis_extraire(tab_distance, k):
    """
    Parameters
    ----------
    tab_distance un tableau de tuple (distance entre deux  enregistrements
    , étiquette) renvoyé par table_distance_nouveau
    
    Returns
    -------
    tableau k_voisins des k plus petits éléments de tab_distance
    selon le critère de distance
    """
    #précondition
    assert k <= len(tab_distance)
    #tri selon la première composante de chaque tuple (la distance)
    tab_tri = sorted(tab_distance, key = clef_tri)
    "à compléter "
    







def element_majoritaire(k_voisins):
    """
    Parameters
    ----------
    k_voisins : tableau des k plus proches voisins 
    
    Returns
    -------
    voisin_majoritaire : chaine de caractère type str, étiquette majoritaire
    parmi les voisins
    """
    occurence = dict()
    voisin_majoritaire = k_voisins[0]
    for voisin in k_voisins:
        if voisin not in occurence:
            occurence[voisin] = 1
        else:
            "à compléter "
            
            
        if voisin != voisin_majoritaire and occurence[voisin] > occurence[voisin_majoritaire]:
            "à compléter "
            
            
    return voisin_majoritaire    



def etiquetage_knn(table, nouveau, etiquette, tab_descripteur, k,
                   distance = distance_euclidienne):
    """
    Parameters
    ----------
    table : tableau de dictionnaires
        table d'enregistrements
    nouveau : un dictionnaire
        un nouvel enregistrement
    etiquette : une chaine de caractères
        le nom du descripteur d'étiquette
    tab_descripteur : un tableau
        liste des noms des descripteurs utilisés pour la comparaison
    k : un entier
        le nombre de voisins examinés
    distance : une fonction distance
        The default is distance_euclidienne.

    Returns
    -------
    voisin_majoritaire : une chaine ce caractère
        l'étiquette majoriataire parmi les k plus proches voisins
    """
    "à compléter "
    
    
    
    
    
    
    
#%% Tests unitaires sur le jeu de données pokemons.csv


#chargement de la table
table_pokemons = charger_fichier_entete('./datas/pokemons.csv')
#postcondition
assert table_pokemons[0] == {'nom': 'Rattata',
                             'vie': '30',
                             'attaque': '56',
                             'defense': '35',
                             'vitesse': '72',
                             'type': 'Normal'}
#filtrage de la table
table_pokemons_feu_roche = [pok for pok in table_pokemons 
                   if pok['type'] in ['Roche', 'Feu']]
#Nouveau Pokemon
nouveau_pokemon = {'vitesse':58, 'attaque' : 120 , 
                   'defense' : 65, 'vie' : 100 }

#Affichage des données
afficher_donnees_point(['vitesse', 'defense'], 'type', 
                        table_pokemons_feu_roche, 
                        point = [58,65], 
                        fichier = 'test-unitaire-pokemons-roche-feu.png')
    
def test_unitaire_distance_euclidienne():
    #Distance avec le pemier pokemon de la table
    salameche = table_pokemons_feu_roche[0]
    assert distance_euclidienne(nouveau_pokemon, 
          salameche, ['vitesse', 'defense']) == 23.087
    print("Test unitaire distance_euclidienne réussi")
    
def test_unitaire_table_distance_nouveau():
    tab_distance = table_distance_nouveau(table_pokemons_feu_roche, nouveau_pokemon,
                           distance_euclidienne,
                           'type', ['vitesse', 'defense'])
    assert tab_distance[:4] == [(23.087, 'Feu'), (23.087, 'Feu'),
                                (25.962, 'Feu'), (43.174, 'Feu')]
    print("Test unitaire table_distance_nouveau réussi")


def test_unitaire_trier_puis_extraire():
    tab_distance = table_distance_nouveau(table_pokemons_feu_roche, nouveau_pokemon,
                           distance_euclidienne,
                           'type', ['vitesse', 'defense'])
    resultat = ['Roche', 'Feu', 'Feu', 'Feu', 'Feu']
    for k in range(1, 6):
        assert trier_puis_extraire(tab_distance, k) == resultat[:k]
    print("Test unitaire trier_puis_extraire réussi")
        

def test_unitaire_element_majoritaire():
    tab_distance = table_distance_nouveau(table_pokemons_feu_roche, nouveau_pokemon,
                           distance_euclidienne,
                           'type', ['vitesse', 'defense'])
    resultat = ['Roche', 'Roche', 'Feu', 'Feu', 'Feu']
    for k in range(1, 6):
        k_voisins = trier_puis_extraire(tab_distance, k)
        assert element_majoritaire(k_voisins) == resultat[k  - 1]
    print("Test unitaire element_majoritaire réussi")
        
def test_unitaire_etiquetage_knn():
    resultat = ['Roche', 'Roche', 'Feu', 'Feu', 'Feu',
                'Feu', 'Feu', 'Feu', 'Feu', 'Feu']
    for k in range(1, 11):
        assert etiquetage_knn(table_pokemons_feu_roche, 
            nouveau_pokemon, 'type', ['vitesse', 'defense'], k) == resultat[k - 1]
    print('Test unitaire etiquetage_knn réussi')
    
   


#Décommentez les lignes pour exécuter les tests unitaires

#test_unitaire_distance_euclidienne()
#test_unitaire_table_distance_nouveau()
#test_unitaire_trier_puis_extraire()
#test_unitaire_element_majoritaire()
#test_unitaire_etiquetage_knn()


#%% Partie 2 : jeu de données iris

#%% Tests unitaires de la partie 2 jeu de données des iris

#chargement de la table
table_iris = charger_fichier_entete('./datas/iris.csv')


def test_unitaire_chargement_iris():
    assert  table_iris[0] == {'id': '1',
                             'longueur_sepale': '5.1',
                             'largeur_sepale': '3.5',
                             'longueur_petale': '1.4',
                             'largeur_petale': '0.2',
                             'espece': 'Iris-setosa'}
    assert table_iris[149] == {'id': '150',
                                 'longueur_sepale': '5.9',
                                 'largeur_sepale': '3.0',
                                 'longueur_petale': '5.1',
                                 'largeur_petale': '1.8',
                                 'espece': 'Iris-virginica'}
    
test_unitaire_chargement_iris()


#%% Partie 3 Optimisation pour les jeux de données très grands et influence de k


#%% Question 1

table_nettoyage = charger_fichier_entete('./datas/nettoyage.csv')
afficher_donnees(["x", "y"], 
                 'nettoyage', table_nettoyage, 
                 fichier = 'nettoyage.png')


#%% Question 2

def distance_manhattan(enreg_a, enreg_b, tab_descripteur):
    """
    Parameters
    ----------
        enreg_a, enreg_b et deux enregistrements de données sous forme de 
        dictionnaires
        tab_descripteur un tableau de descripteurs (certaines clefs des 
                                                    enregistrements)
    
    Returns
    -------
        distance de manhattan entre enreg_a et enreg_b selon les valeurs des 
        descripteurs de tab_descripteur arrondie à 3 chiffres après la virgule
    """
    distance = 0
    for descripteur in tab_descripteur:
        distance = "à  compléter"
    return distance

def test_unitaire_distance_manhattan():
    table_nettoyage = charger_fichier_entete('./datas/nettoyage.csv')
    assert distance_manhattan(table_nettoyage[0], table_nettoyage[1], ['x', 'y']) == 14.0
    assert distance_manhattan(table_nettoyage[10], table_nettoyage[100], ['x', 'y']) == 101.0
    assert distance_manhattan(table_nettoyage[10], table_nettoyage[10], ['x', 'y']) == 0.0
    print('Test unitaire pour distance_manhattan réussi')
    
#Désactivez la ligne suivante pour exécuter le test unitaire
test_unitaire_distance_manhattan()


#%% Question 3


table_nettoyage = charger_fichier_entete('./datas/nettoyage.csv')
afficher_donnees(["x", "y"], 'nettoyage', table_nettoyage, 
                 fichier = 'nettoyage.png')

nouveau_client = {'x' : 30, 'y' : 43}
for k in range(1, 11):
    prediction = "à compléter"
    print("k = ", k, "prédiction  :", prediction)

#%% Question 5

def trier_puis_extraire_insertion(tab_distance, k):
    """
    Parameters
    ----------
    tab_distance un tableau de tuple (distance entre deux  enregistrements
    , étiquette) renvoyé par table_distance_nouveau
    
    Returns
    -------
    tableau k_voisins des k plus petits éléments de tab_distance
    selon le critère de distance
    """
    #précondition
    assert k <= len(tab_distance)
    #liste triée des k premiers tuples de tab_distance 
    k_voisins = sorted([tab_distance[i] for i in range(k)])
    #parcours des tuples suivants
    for i in range(k, len(tab_distance)):     
        nouveau = tab_distance[i]
        #ajout de nouveau à la fin de tab_distance
        k_voisins.append(nouveau)
        #insertion de nouveau à sa place dans la liste triée k_voisins
        #comme dans le tri par insertion avec une boucle while
        j = k - 1
        "à compléter"
        
        
        
        #invariant : ici k_voisins toujours dans l'ordre croissant des distances
        #on enlève le  dernier tuple de k_voisin = voisin le plus loin
        k_voisins.pop()
    #on extrait de k_voisins la liste des étiquettes uniquement
    return [voisin[1] for voisin in k_voisins[:k]]

def test_unitaire_trier_puis_extraire_insertion():
    tab_test1 = [(4, 'paul'), (3, 'jules'), (1, 'paul'), (2, 'jules')]
    assert trier_puis_extraire_insertion(tab_test1, 3) == ['paul', 'jules','jules']
    tab_test2 = [(1, 'paul'), (2, 'jules'), (3, 'paul'), (3, 'jules'), ]
    assert trier_puis_extraire_insertion(tab_test2, 3) == ['paul', 'jules','paul']


#Décommentez pour exécuter le test unitaire
#test_unitaire_trier_puis_extraire_insertion()   
    


def etiquetage_knn_insertion(table, nouveau, etiquette, tab_descripteur, k,
                   distance = distance_euclidienne):
    """
    Parameters
    ----------
    table : tableau de dictionnaires
        table d'enregistrements
    nouveau : un dictionnaire
        un nouvel enregistrement
    etiquette : une chaine de caractères
        le nom du descripteur d'étiquette
    tab_descripteur : un tableau
        liste des noms des descripteurs utilisés pour la comparaison
    k : un entier
        le nombre de voisins examinés
    distance : une fonction distance
        The default is distance_euclidienne.

    Returns
    -------
    voisin_majoritaire : une chaine ce caractère
        l'étiquette majoriataire parmi les k plus proches voisins
    """
    "à compléter"
    
    
def test_unitaire_etiquetage_knn_insertion():
    table_nettoyage = charger_fichier_entete('./datas/nettoyage.csv')
    nouveau_client = {'x' : 30, 'y' : 43}
    for k in range(1, 11):
        prediction1 = etiquetage_knn(table_nettoyage , nouveau_client,'nettoyage', 
                    ['x', 'y'],k,)
        prediction2 = etiquetage_knn_insertion(table_nettoyage , nouveau_client,'nettoyage', 
                    ['x', 'y'],k)
        assert prediction1 == prediction2

#Décommentez pour exécuter le test unitaire
#test_unitaire_etiquetage_knn_insertion()   
    

    

#%% Question 6


def mesure_temps(fonction_etiquetage, k):
    cote_ville = 100
    nouveau_client = {'x' : random.randint(0, cote_ville ), 
                      'y' : random.randint(0, cote_ville )}
    temps_precedent = 0
    ratio = None
    for taille, nom in [(100, 'cent'), (1000,'mille'), (10000, 'dix-mille'), 
                        (100000, 'cent-mille'), (1000000, 'million')]:
        cote_ville  = taille
        fichier = './datas/nettoyage-' + nom + '.csv'
        generer_fichier_aleatoire(taille, cote_ville, fichier)
        table_nettoyage = charger_fichier_entete(fichier)
        debut = time.perf_counter()
        etiquette = fonction_etiquetage(table_nettoyage, nouveau_client,
                                             'nettoyage',  ["x", "y"], k, 
                                             distance_manhattan)
        temps = time.perf_counter() - debut
        if temps_precedent > 0:
            ratio = temps / temps_precedent       
        print("Taille : ", taille, " Temps : ", temps, 
              "Ratio = temps/ temps_precedent =", ratio)
        temps_precedent = temps 
        
#Désactivez pour exécuter les tests de mesure de temps
#mesure_temps(etiquetage_knn_insertion, 5)
#mesure_temps(etiquetage_knn, 5)


#%%Question 5


def influence_k(nb_clients,  cote_ville):
    """
    Parameters
    ----------
    nb_clients : entier représentant le nombre d'immeubles
    cote_ville : entier représentant le cote du plan carré de la ville

    Returns
    -------
    None : procédure qui prédit l'étiquette pour tous les immeubles de la ville
    avec l'algorithme des k plus proches voisins, k variant de 1 à 10 puis
    affiche la carte des prédictions.
    Si l'immeuble est déjà dans le jeu de données on fait quand même une
    prédiction à partir des k plus proches voisins, qui peut être différente
    de l'étiquette du point (pas absurde si on considère que c'est une 
    réattribution de marché)

    """
    horodatage = int(time.time())
    fichier = './datas/nettoyage-' + str(horodatage) + '.csv'
    base_fichier = fichier.split('/')[-1].rstrip('.csv')
    generer_fichier_aleatoire(1000, 100, fichier)
    table_nettoyage = charger_fichier_entete(fichier)
    afficher_donnees(["x", "y"], 
                 'nettoyage', table_nettoyage, 
                  base_fichier + '.png')
    for k in range(1, 11):
        fig = plt.figure(figsize = (6, 6))
        ax = fig.add_subplot(111) 
        for x in range(cote_ville):
            for y in range(cote_ville):
                nouveau_client = {'x' : x, 'y' : y}
                etiquette = etiquetage_knn_insertion(table_nettoyage , 
                                    nouveau_client, 'nettoyage',  ['x', 'y'],
                                    k,  distance_manhattan)
                if etiquette == 'paul':
                    ax.plot(x, y, marker = 'o', ls = '', color = 'red')
                else:
                    ax.plot(x, y, marker = 'o', ls = '', color = 'green')
                ax.set_title('Paul en rouge, Jules en vert, k = {}'.format(k))
        plt.savefig(base_fichier + '-' + 'influence-k={}.png'.format(k))

#Désactivez pour lancer le test
influence_k(1000, 100)