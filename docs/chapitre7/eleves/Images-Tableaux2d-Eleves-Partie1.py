#!/usr/bin/env python
# coding: utf-8

"""
TP Images 
Première NSI 2021-2022
Lycée du Parc
"""

#%% Imports de bibliothèques


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


#%% Outils fournis


def dimensions(pix):
    """renvoie les dimensions (Largeur, Hauteur) d'une matrice
    de pixels"""
    return len(pix[0]), len(pix) 

def matrice_to_image(pix, mode = '1', fichier='image.png', res=1):
    """Convertit en image  une matrice de pixels pix 
    de dimensions (ligne, colonnes)=(nline, ncol)
    en représentant sur l'écran chaque case de pix
    par un carré de coté resolution pixels.
    Le mode de l'image peut être :
    '1'  : binaire 0 ou 1
    'L' : niveaux de gris entre 0 et 255
    'RGB' : triplet de valeurs (Rouge, Vert, Bleu) entre 0 et 255
    """
    #on force la conversion en type np.uint8 si pix est un tableau numpy
    if isinstance(pix, np.ndarray):
        pix = pix.astype(np.uint8)
    #précondition 1 : list doit être une matrice de pixels
    precondition1 = isinstance(pix, (list, np.ndarray))  and len(pix) > 0  and all(isinstance(pix[k], (list, np.ndarray))                         and  len(pix[k]) == len(pix[0])                          for k in range(len(pix)))
    assert precondition1, "Il faut passer en paramètre une matrice de pixels"
    #dimensions de la matrice de pixels
    largeur_pix, hauteur_pix = dimensions(pix)
    #préconditions sur la matrice de pixels pour respecter les contraintes du mode de l'image 
    precondition2 =  mode == '1' and  all(isinstance(pix[y][x], (int, np.uint8)) and 0 <= pix[y][x] <= 1                         for y in range(hauteur_pix) for x in range(largeur_pix))
    precondition3 =  mode == 'L' and  all(isinstance(pix[y][x], (int, np.uint8)) and 0 <= pix[y][x] <= 255                         for y in range(hauteur_pix) for x in range(largeur_pix))
    precondition4 = mode == 'RGB' and all(isinstance(pix[y][x], (list, np.ndarray))                         and len(pix[y][x]) == 3                         and  all(isinstance(pix[y][x][k], (int, np.uint8))                                  and 0 <= pix[y][x][k] <= 255                             for k in range(3))                         for y in range(hauteur_pix) for x in range(largeur_pix))
    assert precondition2 or precondition3 or precondition4, "matrice de pixels et mode incompatibles !"    
    #dimensions de la matrice de pixels
    hauteur_newpix, largeur_newpix = res * hauteur_pix, res * largeur_pix
    #copie de pix sous forme de tableau numpy agrandi d'un coefficient res 
    if mode != 'RGB':
        newpix =  np.zeros((hauteur_newpix, largeur_newpix), dtype='uint8')
    else:
        newpix =  np.zeros((hauteur_newpix, largeur_newpix, 3), dtype='uint8')
    #initialsation des blocs de taille res * res de newpix
    #avec des 0 si pix[i][j] == 0 et 1 sinon
    for y in range(hauteur_newpix):
        for x in range(largeur_newpix):
            ypix = y // res
            xpix = x // res
            newpix[y][x] = pix[ypix][xpix]   
    if mode != 'RGB':
        #création d'un objet image PIL en mode binaire (pixel de valeur 0 ou 1)
        im = Image.new(mode, (largeur_newpix, hauteur_newpix))  #Image.new(mode, (Largeur, Hauteur))  
        #on remplit l'image avec les valeurs de newpix
        im.putdata(newpix.flatten())
    else:
        im = Image.fromarray(newpix)
    #enregistrement de l'image sur le disque
    im.save(fichier)
    #affichage de l'image
    #plt.axis('off') #to disable xticks and yticks
    #cas des images binaires 
    if mode == '1':
        plt.imshow(newpix,cmap=plt.cm.gray, vmin= 0, vmax = 1)
    # cas des images en niveaux de gris
    elif mode == 'L':
        plt.imshow(newpix,cmap=plt.cm.gray, vmin= 0, vmax = 255)
    #cas des images RGB
    else:
        plt.imshow(newpix)
        
def image_to_matrice(fichier):
    #ouverture de l'image avec PIL
    im = Image.open(fichier)
    #conversion de l'image en matrice de pixels / tableau numpy
    pix = np.array(im, dtype = np.uint8)
    #conversion de la matrice de pixels en liste Python
    pix = pix.tolist()
    return pix




#%% Exercice 1
        
pix = [[1, 0, 1, 0], [0, 1, 0, 1]]
matrice_to_image([[1,0,1,0],[0,1,0,1]], mode = '1', fichier='exemple_binaire_4x2.png',res=1)
        

#%% Exemples du point Méthode pages 3, 4 et 5

#%% Définition de tableaux à plusieurs dimensions

t1 = [[1,2], [3,4]]     #tableau/matrice à 2 dimensions
print("t1 = [[1,2], [3,4]] ", "affichage : ",t1, sep ="\n")

print('*' * 80)

t2 = [[1,2], [3,4],[5,6,7]] #tableau à 2 dimensions
print("t2 = [[1,2], [3,4],[5,6,7]]", "affichage : ",t2, sep ="\n")

print('*' * 80)

t3 = [[[1], [2,3]],[4,5,6],[7]]  #tableau mixte 
print("t3 = [[[1], [2,3]],[4,5,6],[7]]", "affichage : ",t3, sep="\n")

print('*' * 80)

print("Longueur de t2 : ", "affichage : ",len(t2), sep="\n")    #t2 contient 2 tableaux éléments
print("Longueur de la première ligne de t2 notée t2[0] ", "affichage : ",len(t2[0]), sep="\n")#t2[0] est un tableau contenant 2 entiers
print("Longueur de la troisième ligne de t2 notée t2[2] ", "affichage : ",len(t2[2]), sep="\n")


print('*' * 80)

t4 = [[0] * 3 for _ in range(2)]
print("t4 = [[0] * 3 for _ in range(2)]", "affichage : ",t4, sep ="\n")

print('*' * 80)

t5 = [[ [0] * 4 for i in range(3)] for j in range(2)]
print("t5 = [[ [0] * 4 for i in range(3)] for j in range(2)]", "affichage : ",t5, sep ="\n")

#%% Parcours de tableaux à plusieurs dimensions
print('*' * 80)
def parcours_tableau2d_index(tab):
    """Parcours par index d'un tableau à 2 dimensions"""
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print('Element en ligne {} colonne {} : '.format(i,j),tab[i][j])
            
def parcours_tableau2d_element(tab):
    """Parcours par élément d'un tableau à 2 dimensions"""
    for ligne in tab:
        for element in ligne:
            print(element)

print("Parcours de t1 par index :", "Affichage : ", sep ="\n")
print(t1)
print("Parcours : ")
parcours_tableau2d_index(t1)

print('*' * 80)
print("Parcours de t1 par élément :", "Affichage : ", sep ="\n")
print(t1)
print("Parcours : ")
parcours_tableau2d_element(t1)





#%% Exercice 2



def max_tab2d(tab):
    """Renvoie le maximum d'un tableau à 2 dimensions"""
    maxi = float('-inf')
    for y in range(len(tab)): #boucle sur les lignes
        for x in range(len(tab[y])): # boucle sur les colonnes
            "à compléter"


# Tests unitaires



assert max_tab2d([[-1,-2],[-2,-3,-0.5]]) == -0.5
assert max_tab2d([[1,2],[float('inf'),10]]) == float('inf')
assert max_tab2d([[1,2],[8,0]]) == 8


#%% Exercice 5

def generer_croix(couleur):
    """Paramètre : couleur un tableau de 3 entiers entre 0 et 255
	Valeur renvoyée : None
	Postcondition : enregistre sur le disque l'image d'une croix de couleur
	sur fonds blanc"""
    blanc = [255,255,255]
    ## TO DO
    croix = "à compléter"
    matrice_to_image(croix, mode = 'RGB', res = 100, fichier='croix.png')  


#%% Exercice 6

def matrice_vide(ncol, nlig, mode):
    """Paramètres  : 2 entiers positifs ncol et nlig et un mode d'image de type str
    Précondition : ncol>=0 et nlig>=0 et mode dans ['1', 'L', 'RGB']
    Valeur renvoyée : une matrice de nlig * ncol   pixels dans le mode choisi
    Postcondition : renvoie une matrice de  pixels nuls"""
    assert nlig >= 0 and ncol >= 0 and mode in ['1', 'L', 'RGB']
    #compléter par des tableaux définis en compréhension
    if mode in ['1', 'L']:
        return "à modifier"
    else:               
        return "à modifier"


#%% Exercice 7


def barres_horizontales(nlig, ncol):
    """renvoie la matrice de pixels d'une image
    de dimensions ncol x nlig avec alternance 
    de lignes noires (index pair)
    ou blanches (index impair)"""
    #on crée une matrice vide de bonnes dimensions
    pix = matrice_vide(ncol, nlig)
    for x in range(ncol): #boucle sur les colonnes
        for y in range(nlig): #boucle sur les lignes
            #les lignes d'index paires seront noires
            "à compléter"
    return pix 


#%% Exercice 8

from typing import List

# Q1
def matrice_rgb_to_gris(pix:List[List[List[int]]])->List[List[int]]:
    """Précondition: pix une matrice de pixels rgb
    Valeur renvoyée: une matrice de pixels en niveaux de gris
    Postcondition : renvoie une matrice des luminances des pixels sources"""
    ncol, nlig = dimensions(pix)
    pix_but = matrice_vide(ncol, nlig)
    #à compléter
    return pix_but
    
#test
mandrill_rgb = image_to_matrice('mandrill.png')
mandrill_gris = matrice_rgb_to_gris(mandrill_rgb)
matrice_to_image(mandrill_gris, mode = 'L', fichier='mandrill_gris.png', res=1)



# Q2

def melange_pixel_gris(p1:int, p2:int, coef:float)->int:
    """Précondition : 0<=p1<= 255 et 0 <= p2 <= 255 et 0 <= coef <= 1
    Postcondition : renvoie int(p1 * coef + (1-coef) * p2)"""
    assert  0 <= p1 <= 255 and 0 <= p2 <= 255 and 0 <= coef <= 1
    return int(p1 * coef + (1-coef) * p2)

def melange_matrice_gris(pix1:List[List[int]], pix2:List[List[int]], coef:float)->List[List[int]]:
    """Précondition : pix1 et pix2 deux matrices de pixels en niveaux de gris     de mêmes dimensions et 0 <= coef <= 1""" 
    #à compléter

def melange_progressif(pix1:List[List[int]], pix2:List[List[int]], n:int)->None:
    for k in range(n + 1):
        matrice_to_image(melange_matrice_gris(pix1, pix2,  k/n), mode='L', fichier=f"melange{k}.png")

#test  
darwin = image_to_matrice("darwin_gris.png")
mandrill = image_to_matrice("mandrill_gris.png")
melange_progressif(darwin, mandrill, 10)

#%% Exercice 9

from  typing import List

def changement_echelle(pix:List[List[int]], coef:float)->List[List[int]]:
    """Précondition: pix une matrice de pixels rgb
    Valeur renvoyée: une matrice de pixels en niveaux de gris
    Postcondition : renvoie une matrice de l'image obtenue par changement d'échelle
    de coefficient coef"""
    ncol, nlig = dimensions(pix)
    ncol_but, nlig_but = int(ncol * coef), int(nlig * coef)
    #à compléter

#code client
mandrill_gris = image_to_matrice('mandrill_gris.png')
mandrill_gris_quart = changement_echelle(mandrill_gris, 0.25)
matrice_to_image(mandrill_gris_quart, mode = 'L', fichier='mandrill_gris_quart.png', res=1)