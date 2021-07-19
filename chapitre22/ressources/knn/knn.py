#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fonctions pour l'algorithme knn
Created on Tue Dec 29 14:01:02 2020
@author: junier
"""

import math


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
        descripteurs de tab_descripteur
    """
    distance_carre = 0
    for descripteur in tab_descripteur:
        distance_carre = distance_carre + (float(enreg_a[descripteur]) - float(enreg_b[descripteur])) ** 2
    return round(math.sqrt(distance_carre), 3)


def table_distance_nouveau(table, nouveau, distance, etiquette, tab_descripteur):
    """
    Parameters
    ----------
    table : une table d'enregistrements de type dictionnaire
    nouveau : un nouvel enregistrement de type dictionnaire
    distance : une fonnction de distance entre deux enregistrements
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
        tab_distance.append((distance(enreg, nouveau, tab_descripteur), enreg[etiquette]))
    return tab_distance

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
    tab_tri = sorted(tab_distance)
    k_voisins = [tab_tri[i][1] for i in range(k)]
    return k_voisins

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
            occurence[voisin] = occurence[voisin] + 1
        if voisin != voisin_majoritaire and occurence[voisin] > occurence[voisin_majoritaire]:
            voisin_majoritaire = voisin
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
    tab_distance = table_distance_nouveau(table, nouveau, distance, etiquette, tab_descripteur)
    k_voisins = trier_puis_extraire(tab_distance, k)
    voisin_majoritaire = element_majoritaire(k_voisins)
    return voisin_majoritaire
    
