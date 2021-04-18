import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

def charger_fichier_entete(nom_fic, separateur = ',', encodage = 'utf-8'):
    """
    Permet de lire un fichier CSV en utilisant la ligne d'entêtes
    Retourne une liste de dictionnaires.
    """
    table = []
    with open(nom_fic , "r", newline ="", encoding = encodage) as csvfile :
        lecteur = csv.DictReader(csvfile , delimiter = separateur)
        for enreg in lecteur :
            table.append (dict(enreg)) # enreg est de type OrderedDict on le remet endict
    return table


def normaliser_fichier(fich_source, fich_sortie, tab_descripteur, separateur = ',', encodage = 'utf-8'):
    """
    Permet de lire un fichier CSV en utilisant la ligne d'entêtes
    Normalise les colonnes de tous les descripteurs de type numérique 
    listés dans tab_descripteur
    avec la formule (valeur - valeurMin)/(valeurMax - valeurMin)
    Ecrit la table normalisée dans fich_sortie
    """
    
    table = []
    colonnes_max = {descripteur : -float('inf') for descripteur in tab_descripteur}
    colonnes_min = {descripteur : float('inf') for descripteur in tab_descripteur}
    #lecture du fichier source et mise à jour des min et max pour chaque descripteur de tab_descripteur
    with open(fich_source , "r", newline ="", encoding = encodage) as csvfile :
        lecteur = csv.DictReader(csvfile , delimiter = separateur)
        en_tetes = lecteur.fieldnames
        for enreg in lecteur :
            enreg = dict(enreg) # enreg est de type OrderedDict on le remet endict
            for descripteur in enreg:
                if descripteur in tab_descripteur:
                    valeur = float(enreg[descripteur])
                    colonnes_max[descripteur] = max(colonnes_max[descripteur], valeur)
                    colonnes_min[descripteur] = min(colonnes_min[descripteur], valeur)
            table.append(enreg)
    #normalisation des colonnes ciblées par tab_descripteur
    for enreg in table:
        for descripteur in tab_descripteur:
            vmin = colonnes_min[descripteur]
            vmax = colonnes_max[descripteur]
            if vmax > vmin:
                amplitude = vmax - vmin
            else:
                amlitude = 1
            valeur = float(enreg[descripteur])
            enreg[descripteur] = str((valeur - vmin) / amplitude)
    #écriture dans le fichier de sortie
    with open(fich_sortie, 'w', newline='', encoding = encodage) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = en_tetes, delimiter = separateur)
        writer.writeheader()
        for enreg in table:
            writer.writerow(enreg)
    
def extraire_colonnes(tab_descripteur, etiquette, table):
    """
    Extrait les colonnes d'une table correspondant aux descripteurs
    listés dans tab_descripteur
    Etiquette est le descripteur d'étiquetage de chaque enregistrement
    Renvoie un dictionnaire de dictionnaires de tableaux, associant 
    à chaque valeur d'etiquette un dictionnaire de clef un descripteur
    et de valeur la colonne des valeurs de ce descripteur sous forme de tableau
    """
    colonnes = dict()
    for enreg in table:
        valeur_etiquette = enreg[etiquette]
        if valeur_etiquette not in colonnes:
            colonnes[valeur_etiquette] = {descripteur : [float(enreg[descripteur])] for descripteur in tab_descripteur}
        else:
            for descripteur in tab_descripteur:
                colonnes[valeur_etiquette][descripteur].append(float(enreg[descripteur])) 
    return colonnes

def afficher_une_colonne(x, colorc, labelc, ax):
    """Affichage d'une colonne de valeurs sur un axe à 1 dimension"""
    ax.plot(x, [0] * len(x), linestyle = ' ', marker = 'o', label = labelc, color = colorc)
    
    
def afficher_deux_colonnes(x, y, colorc, labelc, ax):
    """Affichage de deux colonnes de valeurs dans le plan 
    à 2 dimensions"""
    ax.plot(x, y, linestyle = ' ', marker = 'o', label = labelc, color = colorc)
    
    
def afficher_trois_colonnes(x, y, z, colorc, labelc, ax):
    """Affichage de trois colonnes de valeurs dans l'espace
    à 3 dimensions"""
    ax.scatter(x, y, z, marker = 'o', label = labelc, color = colorc)

MODE_AFFICHAGE = {1 : afficher_une_colonne, 2 : afficher_deux_colonnes, 3 : afficher_trois_colonnes} 


def palette_couleur(n):
    """Génération d'une palette de n couleurs"""
    if n <= 6:
        return ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'black', 'maroon']
    rouge = random.randint(0, 255)
    vert = random.randint(0, 255)
    bleu = random.randint(0, 255)
    palette = []
    for _ in range(n):
        rouge = (rouge + 135) % 256
        vert = (vert + 81) % 256
        bleu = (bleu + 27) % 256
        palette.append('#' + ''.join([hex(composante).lstrip('0x').zfill(2)  
                                        for composante in [rouge, vert ,bleu]])
                                        )
    return palette
    
def afficher_donnees(tab_descripteur, etiquette, table, fichier = 'output.png'):
    """Affichage des données contenues dans table
    En prenant pour descripteurs de valeurs ceux listés dans tab_descripteur
    Etiquette est le descripteur d'étiquetage de chaque enregistrement
    Fichier est le fichier de sortie du graphique    
    """
    dimension = len(tab_descripteur)
    assert dimension <= 3
    colonnes = extraire_colonnes(tab_descripteur, etiquette, table)
    couleur = palette_couleur(len(colonnes))
    fig = plt.figure(figsize = (6, 6))
    if dimension == 3:
        ax = fig.add_subplot(111, projection='3d') 
    else:
        ax = fig.add_subplot(111) 
    index_couleur = 0
    for etiquette, colonnes in extraire_colonnes(tab_descripteur, etiquette, table).items():
        MODE_AFFICHAGE[dimension](*[col for descripteur, col in colonnes.items()], couleur[index_couleur],
                                    etiquette, ax)
        index_couleur = (index_couleur + 1) % len(couleur)
    ax.set_xlabel(tab_descripteur[0])
    if dimension >= 2:
        ax.set_ylabel(tab_descripteur[1])
    if dimension == 3:
        ax.set_zlabel(tab_descripteur[2])
    ax.legend(loc = 'lower right')
    plt.savefig(fichier)
    plt.show()


def afficher_donnees_point(tab_descripteur, etiquette, table, point, fichier = 'output.png'):
    """Pareil que afficher_donnees
    mais affiche en plus un nouveau point qui n'est pas dans table
    """    
    dimension = len(tab_descripteur)
    assert dimension <= 3
    colonnes = extraire_colonnes(tab_descripteur, etiquette, table)
    couleur = palette_couleur(len(colonnes))
    fig = plt.figure(figsize = (6, 6))
    if dimension == 3:
        ax = fig.add_subplot(111, projection='3d') 
    else:
        ax = fig.add_subplot(111) 
    index_couleur = 0
    for etiquette, colonnes in extraire_colonnes(tab_descripteur, etiquette, table).items():
        MODE_AFFICHAGE[dimension](*[col for descripteur, col in colonnes.items()], couleur[index_couleur],
                                    etiquette, ax)
        index_couleur = (index_couleur + 1) % len(couleur)
    ax.set_xlabel(tab_descripteur[0])
    if dimension >= 2:
        ax.set_ylabel(tab_descripteur[1])
    if dimension == 3:
        ax.set_zlabel(tab_descripteur[2])
    ax.legend(loc = 'best')
    ax.plot(*point, marker = 'x', markersize = 10, markeredgewidth=5, color = "orange")
    plt.savefig(fichier)
    plt.show()
